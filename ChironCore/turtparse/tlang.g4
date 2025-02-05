
grammar tlang;

start : instruction_list EOF
      ;

instruction_list : (instruction)*
		 ;

strict_ilist : (instruction)+
             ;

instruction : assignment
	    | conditional
	    | loop
	    | moveCommand
	    | penCommand
	    | gotoCommand
	    | pauseCommand
		| declaration
		| struct_definition
	    ;

struct_definition : STRUCT VAR '{' declaration_list assignment_list '}' ;

declaration_list : (declaration)+ ;

declaration : array_declaration | variable_declaration ;

assignment_list : (assignment)* ;

// value of 'expression` should be known at compile time
array_declaration : data_type VAR '[' expression ']' ;

variable_declaration : data_type VAR ;

data_type : INT | custom ;

custom : STRUCT VAR ;

INT : 'int' ;
STRUCT: 'struct' ;

conditional : ifConditional | ifElseConditional ;

ifConditional : 'if' condition '[' strict_ilist ']' ;

ifElseConditional : 'if' condition '[' strict_ilist ']' 'else' '[' strict_ilist ']' ;

loop : 'repeat' value '[' strict_ilist ']' ;

gotoCommand : 'goto' '(' expression ',' expression ')';

assignment :  varAssignment | arrayAssignment | memberAssignment | arrayMemberAssignment 
	   ;
varAssignment : VAR '=' expression ;

memberAssignment : member '=' expression ;

arrayMemberAssignment : array_member '=' expression ;

// raise error when number of values doesnt match the declared array size
arrayAssignment : VAR '=' '{' (expression (',' expression)*)? '}' ;

moveCommand : moveOp expression ;
moveOp : 'forward' | 'backward' | 'left' | 'right' ;

penCommand : 'penup' | 'pendown' ;

pauseCommand : 'pause' ;

expression : 
             unaryArithOp expression               #unaryExpr
           | expression multiplicative expression  #mulExpr
		   | expression additive expression        #addExpr
		   | value                                 #valueExpr
		   | '(' expression ')'                    #parenExpr
 	   ;

multiplicative : MUL | DIV;
additive : PLUS | MINUS;

unaryArithOp : MINUS ;

PLUS     : '+' ;
MINUS    : '-' ;
MUL  	 : '*' ;
DIV      : '/' ;


// TODO :
// procedure_declaration : 'to' NAME (VAR)+ strict_ilist 'end' ;

condition : NOT condition
          |expression binCondOp expression
	  | condition logicOp condition
	  | PENCOND
	  | '(' condition ')'
	  ;


binCondOp :  EQ | NEQ | LT | GT | LTE | GTE
	 ;

logicOp : AND | OR ;

PENCOND : 'pendown?';
LT : '<' ;
GT : '>' ;
EQ : '==';
NEQ: '!=';
LTE: '<=';
GTE: '>=';
AND: '&&';
OR : '||';
NOT: '!' ;

value : NUM
      | VAR
	  | member
	  | array_member
      ;

NUM  : [0-9]+        ;

member : VAR ('.' VAR)+ ;

array_member : VAR '[' expression ']' ;

VAR  : ':'[a-zA-Z_] [a-zA-Z0-9]* ;

NAME : [a-zA-Z]+     ;

Whitespace: [ \t\n\r]+ -> skip;
