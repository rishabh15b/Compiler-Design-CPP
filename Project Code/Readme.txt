Section : B


Project Title: Mini Compiler for C++ language


Team Members: Kashish Oberoi(PES1201700113) , Sagar Ratan Garg(PES1201700913) , Vivek Aditya(PES1201701125)


Project Guide : Preet Kanwal, Assistant Professor


Project Abstract: The main functionality of the project is to generate an optimized intermediate code for the given C++ source code and also assembly code using this optimized intermediate code generated.


Code Execution : 

To Execute lex files 	 			: lex <filename.l>
To Execute yacc files	 			: yacc -d <filename.y>
To Compile C files generated    		: gcc lex.yy.c y.tab.c -ll
Final Output		           			: ./a.out < inputfile.c
To Test Optimizing Code written in Python	: python3 <filename.py> < testicgfile.txt