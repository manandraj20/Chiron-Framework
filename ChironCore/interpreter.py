
from ChironAST import ChironAST
from ChironHooks import Chironhooks
import turtle
import re
Release="Chiron v5.3"

def addContext(s):
    s= re.sub(r'(?<!\.):', 'self.prg.', str(s).strip())
    s= str(s).strip().replace(":", "")

    return s


class Interpreter:
    # Turtle program should not contain variable with names "ir", "pc", "t_screen"
    ir = None
    pc = None
    t_screen = None
    trtl = None

    def __init__(self, irHandler, params):
        self.ir = irHandler.ir
        self.cfg = irHandler.cfg
        self.pc = 0
        self.t_screen = turtle.getscreen()
        self.trtl = turtle.Turtle()
        self.trtl.shape("turtle")
        self.trtl.color("blue", "yellow")
        self.trtl.fillcolor("green")
        self.trtl.begin_fill()
        self.trtl.pensize(4)
        self.trtl.speed(1) # TODO: Make it user friendly

        if params is not None:
            self.args = params
        else:
            self.args = None

        turtle.title(Release)
        turtle.bgcolor("white")
        turtle.hideturtle()

    def handleAssignment(self, stmt,tgt):
        raise NotImplementedError('Assignments are not handled!')

    def handleCondition(self, stmt, tgt):
        raise NotImplementedError('Conditions are not handled!')

    def handleMove(self, stmt, tgt):
        raise NotImplementedError('Moves are not handled!')

    def handlePen(self, stmt, tgt):
        raise NotImplementedError('Pens are not handled!')

    def handleGotoCommand(self, stmt, tgt):
        raise NotImplementedError('Gotos are not handled!')

    def handleNoOpCommand(self, stmt, tgt):
        raise NotImplementedError('No-Ops are not handled!')

    def handlePauseCommand(self, stmt, tgt):
        raise NotImplementedError('No-Ops are not handled!')

    def sanityCheck(self, irInstr):
        stmt, tgt = irInstr
        # if not a condition command, rel. jump can't be anything but 1
        if not isinstance(stmt, ChironAST.ConditionCommand) and not isinstance(stmt, ChironAST.FunctionDeclarationCommand):
            if tgt != 1:
                raise ValueError("Improper relative jump for non-conditional instruction", str(stmt), tgt)
    
    def interpret(self):
        pass

    def initProgramContext(self, params):
        pass

class ProgramContext:
    pass

class ClassList:
    pass

# TODO: move to a different file
class ConcreteInterpreter(Interpreter):
    # Ref: https://realpython.com/beginners-guide-python-turtle
    cond_eval = None # used as a temporary variable within the embedded program interpreter
    prg = None
    argument = None
    return_value = None
    class_list = None

    # map of function name to their pc in the IR
    function_addresses = {}
    #stack for handling function calls
    call_stack = []

    def __init__(self, irHandler, params):
        super().__init__(irHandler, params)
        self.prg = ProgramContext()
        self.class_list = ClassList()
        # Hooks Object:
        if self.args is not None and self.args.hooks:
            self.chironhook = Chironhooks.ConcreteChironHooks()
        self.pc = 0
        print("###########################Intermediate Representation (IR):#############")
        for index, instruction in enumerate(self.ir):
            print(f"{index}: {instruction} | {instruction[0]}")

    def interpret(self):
        print("Program counter : ", self.pc)
        stmt, tgt = self.ir[self.pc]

        print(stmt, stmt.__class__.__name__, tgt)

        self.sanityCheck(self.ir[self.pc])

        if isinstance(stmt, ChironAST.AssignmentCommand):
            ntgt = self.handleAssignment(stmt, tgt)
        elif isinstance(stmt, ChironAST.PrintCommand):
            ntgt = self.handlePrint(stmt, tgt)
        elif isinstance(stmt, ChironAST.ConditionCommand):
            ntgt = self.handleCondition(stmt, tgt)
        elif isinstance(stmt, ChironAST.MoveCommand):
            ntgt = self.handleMove(stmt, tgt)
        elif isinstance(stmt, ChironAST.PenCommand):
            ntgt = self.handlePen(stmt, tgt)
        elif isinstance(stmt, ChironAST.GotoCommand):
            ntgt = self.handleGotoCommand(stmt, tgt)
        elif isinstance(stmt, ChironAST.NoOpCommand):
            ntgt = self.handleNoOpCommand(stmt, tgt)
        elif isinstance(stmt, ChironAST.ClassDeclarationCommand):
            ntgt = self.handleClassDeclaration(stmt, tgt)
        elif isinstance(stmt, ChironAST.ObjectInstantiationCommand):
            ntgt = self.handleObjectInstantiation(stmt, tgt)
        elif isinstance(stmt, ChironAST.FunctionDeclarationCommand):
            ntgt = self.handleFunctionDeclaration(stmt, tgt)
        elif isinstance(stmt, ChironAST.FunctionCallCommand):
            ntgt = self.handleFunctionCall(stmt, tgt)
        elif isinstance(stmt, ChironAST.ReturnCommand):
            ntgt = self.handleFunctionReturn(stmt, tgt)
        elif isinstance(stmt, ChironAST.ParametersPassingCommand):
            ntgt = self.handleParametersPassing(stmt, tgt)
        elif isinstance(stmt, ChironAST.ReadReturnCommand):
            ntgt = self.handleReturnRead(stmt, tgt)
             
        else:
            raise NotImplementedError("Unknown instruction: %s, %s."%(type(stmt), stmt))

        # TODO: handle statement
        self.pc += ntgt

        if self.pc >= len(self.ir):
            # This is the ending of the interpreter.
            self.trtl.write("End, Press ESC", font=("Arial", 15, "bold"))
            if self.args is not None and self.args.hooks:
                self.chironhook.ChironEndHook(self)
            return True
        else:
            return False
    
    def initProgramContext(self, params):
        # This is the starting of the interpreter at setup stage.
        if self.args is not None and self.args.hooks:
            self.chironhook.ChironStartHook(self)
        self.trtl.write("Start", font=("Arial", 15, "bold"))
        for key,val in params.items():
            var = key.replace(":","")
            exec("setattr(self.prg,\"%s\",%s)" % (var, val))
    
    def handleFunctionDeclaration(self, stmt, tgt):
        print(f"Function Declaration: {stmt.name}")
        self.function_addresses[stmt.name] = self.pc + 1
        return tgt
    
    def handleFunctionCall(self, stmt, tgt):
        print("[1]", stmt, "printing stmt")
        if stmt.caller:
            print("FINDING CLASS NAME!###################")
            print("Caller: ", stmt.caller)
            caller_class = eval(addContext(stmt.caller)).__class__.__name__
            print(caller_class)
            stmt.name = ":" + str(caller_class)+ "@" + str(stmt.name)
        self.call_stack.append(self.pc + 1)
        # Save the current program context
        self.call_stack.append(self.prg)
        # Initialize a new program context for the function call
        for arg in stmt.args:
            arg_value = addContext(arg)
            exec(f"self.argument = {arg_value}")
            self.call_stack.append(self.argument)
        self.prg = ProgramContext()
        self.pc = self.function_addresses[stmt.name]
        return 0
    
    def handleReturnRead(self, stmt, tgt):
        print(f"Read Return: {stmt.returnValues}")
        for rval in reversed(stmt.returnValues):
            rval = str(rval).replace(":", "")
            exec(f"self.prg.{rval} = self.call_stack.pop()")
        return 1

    def handleFunctionReturn(self, stmt, tgt):
        print(f"Function Return: {stmt}")
        # Restore the previous program context
        rval_list = []
        for rval in stmt.returnValues:
            rval_value = addContext(rval)
            exec(f"self.return_value = {rval_value}")
            rval_list.append(self.return_value)
        self.prg = self.call_stack.pop()
        self.pc = self.call_stack.pop()
        self.call_stack.extend(rval_list)
        return 0
    

    def handleParametersPassing(self, stmt, tgt):
        print(f"Parameters Passing: {stmt.params}")
        for param in reversed(stmt.params):
            param = str(param).replace(":", "")
            param_value = self.call_stack.pop()
            print("PRINTING PARAM VALUE###############", param_value, param)
            setattr(self.prg, param, param_value)
            print("PRINTING PARAM VALUE###############", getattr(self.prg, param))
        return 1

    def handleClassDeclaration(self, stmt, tgt):
        print(f"Class Declaration: {stmt.className}")

        className = stmt.className.replace(":", "")
        attributes = stmt.attributes  # List of attribute assignments

        # Handle inheritance if base classes exist
        if hasattr(stmt, "baseClasses") and stmt.baseClasses:
            # Build a comma-separated list of base classes.
            # We assume the base classes are already stored in self.class_list.
            base_classes = [getattr(self.class_list, str(b).replace(":","")) for b in stmt.baseClasses]
            base_str = ", ".join([b.__name__ for b in base_classes])
            class_header = f"class {className}({base_str}):\n"

        else:
            class_header = f"class {className}:\n"

        class_def = class_header

        # Handle normal attributes
        for attr in attributes:
            attr, target = attr
            attr_name = str(attr.lvar).replace(":", "")
            attr_value = addContext(attr.rexpr) if attr.rexpr else None
            class_def += f"    {attr_name} = {attr_value}\n"

        # Handle object attributes (initialize to None first)
        for objectAttr in stmt.objectAttributes:
            objectAttr, target = objectAttr
            lhs = str(objectAttr.target).replace(":", "")
            class_def += f"    {lhs} = None\n"

        print(class_def, "Class Definition")

        # Step 1: Execute the class definition (store it inside self.class_list)
        exec(class_def, globals(), self.class_list.__dict__)

        # Step 2: Assign object attributes after class creation
        for objectAttr in stmt.objectAttributes:
            objectAttr, target = objectAttr
            lhs = str(objectAttr.target).replace(":", "")
            rhs = addContext(objectAttr.class_name).replace("self.prg.", "self.class_list.")
            exec(f"self.class_list.{className}.{lhs} = {rhs}()")

        return 1


    def handleObjectInstantiation(self, stmt, tgt):
        print(f"Creating new instance of {stmt.class_name} for {stmt.target}")

        lhs = str(stmt.target).replace(":","")
        rhs = addContext(stmt.class_name).replace("self.prg.", "self.class_list.")

        # exec(instance_code, globals(), self.prg.__dict__)  # Store in self.prg
        exec(f"self.prg.{lhs} = {rhs}()")
        print(f"Instance created: {lhs} -> {getattr(self.prg, lhs)}")

        return 1

    
    
    def handleAssignment(self, stmt, tgt):
        print("  Assignment Statement")
        lhs = str(stmt.lvar).replace(":","")
        rhs = addContext(stmt.rexpr)
        print(lhs,rhs,"Assignment")
        # exec("setattr(self.prg,\"%s\",%s)" % (lhs,rhs))
        exec(f"self.prg.{lhs} = {rhs}")
        return 1
    
    def handlePrint(self,stmt,tgt):
        print( " PrintCommand")
        expr = addContext(stmt.expr)
        print("Executing print with expression:", expr)
        exec("print(%s)" % expr)
        return 1

    def handleCondition(self, stmt, tgt):
        print("  Branch Instruction")
        condstr = addContext(stmt)
        exec("self.cond_eval = %s" % (condstr))
        return 1 if self.cond_eval else tgt

    def handleMove(self, stmt, tgt):
        print("  MoveCommand")
        exec("self.trtl.%s(%s)" % (stmt.direction,addContext(stmt.expr)))
        return 1
    


    def handleNoOpCommand(self, stmt, tgt):
        print("  No-Op Command")
        return 1

    def handlePen(self, stmt, tgt):
        print("  PenCommand")
        exec("self.trtl.%s()"%(stmt.status))
        return 1

    def handleGotoCommand(self, stmt, tgt):
        print(" GotoCommand")
        xcor = addContext(stmt.xcor)
        ycor = addContext(stmt.ycor)
        exec("self.trtl.goto(%s, %s)" % (xcor, ycor))
        return 1
