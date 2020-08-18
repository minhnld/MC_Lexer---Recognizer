import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int main () {} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    def test_more_complex_program(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 202))

    def test_wrong_miss_close(self):
        """Miss ) int main( {}"""
        input = """int main( {}"""
        expect = "Error on line 1 col 10: {"
        self.assertTrue(TestParser.checkParser(input, expect, 203))

    def test_var_declaration_1(self):
        """Var declaration: 1"""
        input = """int a; void main (){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 204))

    def test_var_declaration_2(self):
        """Var declaration: 2"""
        input = """void main(){} string a,b,c; boolean _a; float _c; int minh,a[3]; """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 205))

    def test_var_declaration_3(self):
        """Var declaration: 3"""
        input = """int[3] a[3]; void main (){}"""
        expect = "Error on line 1 col 4: 3"
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    def test_var_declaration_4(self):
        """Var declaration: 4"""
        input = """string ; void main (){}"""
        expect = "Error on line 1 col 7: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 207))

    def test_var_declaration_5(self):
        """Var declaration: 5"""
        input = """int a=3;void main (){} """
        expect = "Error on line 1 col 5: ="
        self.assertTrue(TestParser.checkParser(input, expect, 208))

    def test_var_declaration_6(self):
        """Var declaration: 6"""
        input = """int a[-100];void main (){} """
        expect = "Error on line 1 col 6: -"
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def test_var_declaration_7(self):
        """Var declaration: 7"""
        input = """int abc[m];void main (){} """
        expect = "Error on line 1 col 8: m"
        self.assertTrue(TestParser.checkParser(input, expect, 210))

    ####################################################
    def test_function_declaration_1(self):
        """Function declaration 1"""
        input = """ int foo() {break;} void main(){return;} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    def test_function_declaration_2(self):
        """Function declaration 2"""
        input = """ int foo(int a,b) { int i;} int main(){return;} """
        expect = "Error on line 1 col 15: b"
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    def test_function_declaration_3(self):
        """Function declaration 2"""
        input = """ int foo(float b[],c[],ewqd,minh) { int i;} boolean c,d; void main(){return;} """
        expect = "Error on line 1 col 19: c"
        self.assertTrue(TestParser.checkParser(input, expect, 213))

    def test_function_declaration_4(self):
        """Function declaration 2"""
        input = """ int foo(float b[], string c[], int ewqd, boolean minh) { int i;} boolean c,d; void main(){return;} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def test_function_declaration_5(self):
        """Function declaration 2"""
        input = """ int[] foo(int a, float b[]) {int c[3]; if (a>0) foo(a-1,b); return c; } void main(){return;} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 215))
    def test_function_declaration_6(self):
        """Function declaration 2"""
        input = """ int a,b,c;float d; string[] foo(int a, float b[]) {int c[3]; if (a>0) foo(a-1,b); return c; } void main(){return;} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 216))
    def test_function_declaration_7(self):
        """Function declaration 2"""
        input = """ int float(int a, float b[]) {int c[3]; if (a>0) foo(a-1,b); return c; } void main(){return;} """
        expect = "Error on line 1 col 5: float"
        self.assertTrue(TestParser.checkParser(input, expect, 217))  
    def test_function_declaration_8(self):
        input = """ boolean _; boolean _(int a, float b[]) {int c[3]; if (a>0) foo(a-1,b); return c; } void main(){return;} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 218))  
    def test_function_declaration_9(self):
        input = """ float _; boolean _(float b[],) {int c[3]; if (a>0) foo(a-1,b); return c; } void main(){return;} """
        expect = "Error on line 1 col 30: )"
        self.assertTrue(TestParser.checkParser(input, expect, 219))      
    def test_function_declaration_10(self):
        input = """ float _; boolean _ float b[],,,,,) {int c[3]; if (a>0) foo(a-1,b); return c; } void main(){return;} """
        expect = "Error on line 1 col 20: float"
        self.assertTrue(TestParser.checkParser(input, expect, 220)) 
################################################################
    def test_assignment_statement_1(self):
        input = """  void main(){ a=b; } int a,b,c; """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 221)) 
    def test_assignment_statement_2(self):
        input = """  void main(){ a=b=c; } int a,b,c; """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 222)) 
    def test_assignment_statement_3(self):
        input = """void main(){ a=; } int a,b,c; """
        expect = "Error on line 1 col 15: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 223))
    def test_assignment_statement_4(self):
        input = """int main(){ =a; } int a,b,c; """
        expect = "Error on line 1 col 12: ="
        self.assertTrue(TestParser.checkParser(input, expect, 224))
    def test_assignment_statement_5(self):
        input = """int main(){a=b; b=a; } int a,b,c; """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 225))
    def test_assignment_statement_6(self):
        input = """int main(){ a; } int a,b,c; """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 226))
    def test_assignment_statement_7(self):
        input = """int main(){ a=b=; } int a,b,c; """
        expect = "Error on line 1 col 16: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 227))
#######################################################################
    def test_if_statement_1(self):
        input = """int main(){ if (a=b) {} }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 228))
    def test_if_statement_2(self):
        input = """void main(){ if (a=b) d=0; else a=8; }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 229))
    def test_if_statement_3(self):
        input = """int main(){ if (x) {} }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 230))
    def test_if_statement_4(self):
        input = """int main(){ if (a=b) a=b; {} }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 231))
    def test_if_statement_5(self):
        input = """int main(){ if (x) if (b) b; else c;  {}  }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 232))
    def test_if_statement_6(self):
        input = """int main(){ if (x) else  }  """
        expect = "Error on line 1 col 19: else"
        self.assertTrue(TestParser.checkParser(input, expect, 233))
    def test_if_statement_7(self):
        input = """int main(){ if (x) continue; }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 234))
        ##################################
    def test_while_statement_1(self):
        input = """int main(){ do {} while(a>b);  }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 235))  
    def test_while_statement_2(self):
        input = """int main(){ do foo(); while(a=x);}  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 236))   
    def test_while_statement_3(self):
        input = """int main(){ do while(a=x); }  """
        expect = "Error on line 1 col 15: while"
        self.assertTrue(TestParser.checkParser(input, expect, 237))   
    def test_while_statement_4(self):
        input = """int main(){ do {}{print("statement 1");}{}{} while(true);  }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 238))   
    def test_while_statement_5(self):
        input = """int main(){ do do{} while(x>d);  while(a);  }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 239))   
    def test_while_statement_6(self):
        input = """int main(){ do {} while a; }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 240))   
    def test_while_statement_7(self):
        input = """int main(){ do do a; while a+c+3; }  """
        expect = "Error on line 1 col 34: }"
        self.assertTrue(TestParser.checkParser(input, expect, 241))   
        #################################################################
    def test_for_statement_1(self):
        input = """void main(){ for(a=c=c; a<100; a=b ) {}   }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 242))     
    def test_for_statement_2(self):
        input = """void main(){ for a=c=c; b=d; a=b;  {}   }  """
        expect = "Error on line 1 col 17: a"
        self.assertTrue(TestParser.checkParser(input, expect, 243))     
    def test_for_statement_3(self):
        input = """void main(){ for(a=((c)=c); a ; b ) {{{{}}}}   }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 244))     
    def test_for_statement_4(self):
        input = """void main(){ for(; ; ) {x=x+2; d=d-1;   }  """
        expect = "Error on line 1 col 17: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 245))     
    def test_for_statement_5(self):
        input = """void main(){ for(a=c; a<100; a=a-1 ) {}   }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 246))     
    def test_for_statement_6(self):
        input = """void main(){ for(a=c=c; a<100; a=b ) for(a=xd;d=2 ;e=3  ) {{}}   }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 247))     
    def test_for_statement_7(self):
        input = """void main() { for(a=c=c; a<100; a=b ) {for(d<3;d*3 ;d==3 ){} x=x+3231;} } """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 248))  
#########################################################
    def test_break_statement_1(self):
        input = """void main(){ if (a) break; }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 249))      
    def test_break_statement_2(self):
        input = """void main(){ do if (a==b) break; while(a!=b); }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 250))      
    def test_break_statement_3(self):
        input = """void main(){ for (a=b;c>3;d=d*3) break; }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 251))      
    def test_break_statement_4(self):
        input = """void main(){  break; }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 252))      
    def test_break_statement_5(self):
        input = """void main(){ if (a) a=a+1; else break; }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 253))      
    def test_break_statement_6(self):
        input = """void main(){ if (a) do break; while (false); }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 254))      
    def test_break_statement_7(self):
        input = """void main(){ do if (a==10) b=3; break; while(a); }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 255))  
#########################
    def test_continue_statement_1(self):
        input = """void main(){  if (a) continue; }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 256))     
    def test_continue_statement_2(self):
        input = """void main(){  do continue; while(true); }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 257)) 
    def test_continue_statement_3(self):
        input = """void main(){  for (a;a;a) continue; }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 258)) 
    def test_continue_statement_4(self):
        input = """void main(){ continue; }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 259)) 
    def test_continue_statement_5(self):
        input = """void main(){  if (a) b==b; else continue; }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 260)) 
    def test_continue_statement_6(self):
        input = """void main(){  if (a) do continue; while(b); }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 261)) 
    def test_continue_statement_7(self):
        input = """void main(){  do if(b) a; continue; while(c); }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 262)) 
###################################  
    def test_expression_1(self):
        input = """void main(){  a=b; }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 263)) 
    def test_expression_2(self):
        input = """void main(){  a||b; }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 264)) 
    def test_expression_3(self):
        input = """void main(){  a&&b; }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 265)) 
    def test_expression_4(self):
        input = """void main(){  a==b; }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 266)) 
    def test_expression_5(self):
        input = """void main(){  a!=b; }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 267)) 
    def test_expression_6(self):
        input = """void main(){  a<=b; a<b; a>b; a>=b; }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 268)) 
    def test_expression_7(self):
        input = """void main(){  a+b--c+2321*321-c/d*3421%321151; }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 269)) 
    def test_expression_8(self):
        input = """void main(){  -a; !d;  }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 270)) 
    def test_expression_9(self):
        input = """void main(){  foo(2)[32+x]=a[b[2]]+3; }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 271)) 
    def test_expression_10(self):
        input = """void main(){  a=b; }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 272)) 
    def test_expression_11(self):
        input = """void main(){  124214; -12.53212; !123;  }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 273)) 
    def test_expression_12(self):
        input = """void main(){  (-12.25e-12); }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 274)) 
    def test_expression_13(self):
        input = """void main(){   a[((123))]; }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 275)) 
    def test_expression_14(self):
        input = """void main(){  a[a[a[100]]]; foooooo(314,asdas,14124); }  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 276)) 
    ###########
    def test_all_1(self):
        input = """
        int i; 
        int f(){return 200;} 
        void main(){ 
            int main; 
        {   
            mainx=f(); 
            putIntLn(main);
            main = f = i = 100;
            putIntLn(i);
            putIntLn(main);
            putIntLn(f); 
        } 
        putIntLn(main);
        }
        float k;
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 277)) 
    def test_all_2(self):
        input = """

        void main(){ 
            foo(3,a+123,m(2231));
        }
        int i; 
        int f(){return 200;} 
        float k;
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 278)) 
    def test_all_3(self):
        input = """
      int a,csa,asdad;
        void main(){ 
            int main; 
            float iiint[3123];
            do d=c[a]+b+dasd+21312; while(true);
        }

         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 279)) 
    def test_all_4(self):
        input = """

        void main(){ 
                a=b[100]=foo()[3]=x=1;
        }
        float k;
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 280)) 
    def test_all_5(self):
        input = """
        float i; 
        float f(){ } 
        void main()
        { 
            if (a) 2.3; // dasdsadsadas fasfsajfioajofjoasjf
            else minhdang(fasfsaf,dsadsad); /* ????DASsafjquhrqwur */
        } 
        float k;
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 281)) 
    def test_all_6(self):
        input = """
        int iasd[32]; 
        float[] fuuuc(int b[],int c[]){return 200;} 
        int main(){ 
            if (a) return 12312;
            else break;
        }
        float k;
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 282)) 
    def test_all_7(self):
        input = """
        int iasd[12412]; 
        float fucas[12421]; 
        void main(){ 
            foo (x ); //CORRECT
            foo (y ); //WRONG
            foo (z ); //WRONG 
        }
        float k;
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 283)) 
    def test_all_8(self):
        input = """

        void main(){ 
          int a,b,c,k[3123];
          {
              foo(2)[331-3131*x]=a[b[3]]*312;
          }
        }

         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 284)) 
    def test_all_9(self):
        input = """
        
        void main(){ 
                -2147483648;
                2147483647;
               int asfsafas; float fasf;
        }
       
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 285)) 
    def test_all_10(self):
        input = """
        int i ;
        int f () {
                   return 200;
                }
        void main() {
            int main ;
            main = f ();
            putIntLn(main );
                 {
                    int i ;
                    int main ;
                    int f ;
                    main = f = i = 100;
                    putIntLn( i );
                    putIntLn(main );
                    putIntLn( f );
                }
                putIntLn(main );
            }
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 286)) 
    def test_all_11(self):
        input = """
     
        void main(){ 
            a=a>b<c;  {{}}
        }
        
         """
        expect = "Error on line 4 col 17: <"
        self.assertTrue(TestParser.checkParser(input, expect, 287)) 
    def test_all_12(self):
        input = """
        int[] foo(int a,float c[] ){}
        float x,t,asd;
        void main(){ 
            {{}}
        }
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 288)) 
    def test_all_13(self):
        input = """
        int a[3,4];
        void main(){ 
        }
         """
        expect = "Error on line 2 col 15: ,"
        self.assertTrue(TestParser.checkParser(input, expect, 289)) 
    def test_all_14(self):
        input = """
        int a,c,d;
        int d[3];
        float das[31];
        void main(){ 
         hahaahahaahaha;
         foo(asd,fa[3123],da[]);
        }
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 290)) 
    def test_all_14(self):
        input = """
        int a,c,d;
        int d[3];
        float das[31];
        void main(){ 
         hahaahahaahaha;
         foo(asd,fa[3123],da[foo(3)]);
         das[12];
        }
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 290))
    def test_if_statement_232(self):
        input = """void main(){
        int a;
        if(a == 0) a = 2;
        else if(a == 3) a = 1;
        else
        }"""
        expect = "Error on line 6 col 8: }"
        self.assertTrue(TestParser.checkParser(input, expect, 291)) 
    def test_fun(self):
        input = """void main(){
        foo(foo(foo(foo(foo(4)))));
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 292)) 
##########################
    def test_all_144(self):
        input = """
        int a,b;
        do {
             if (a) break;
        }
        while(x=3);
         """
        expect = "Error on line 3 col 8: do"
        self.assertTrue(TestParser.checkParser(input, expect, 293))
    def test_all_15(self):
        input = """

        void main(){ 

        }
         void main(){ 

        }
         void main(){ 

        }
         void main(){ 

        }
         void main(){ 
        }
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 294))
    def test_all_16(self):
        input = """

        void main(){ 
                 foo(a[]);
        }

         """
        expect = "Error on line 4 col 23: ]"
        self.assertTrue(TestParser.checkParser(input, expect, 295))
    def test_all_17(self):
        input = """

        void main(){ 
                 foo(floata[a[123]]);
        }

         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 296))
    def test_all_18(self):
        input = """

        void main(){ 
                 int[] http(int a[]){}
        }

         """
        expect = "Error on line 4 col 20: ["
        self.assertTrue(TestParser.checkParser(input, expect, 297))
    def test_all_19(self):
        input = """
        void main(){ 
                 for (if(a) b=3;b=3123;d>=312) {do x; while(hihi);} // aasdsaonqiwfnqwiof
        }

         """
        expect = "Error on line 3 col 22: if"
        self.assertTrue(TestParser.checkParser(input, expect, 298))
    def test_all_20(self):
        input = """
        foo();
        void main(){ 
        }

         """
        expect = "Error on line 2 col 8: foo"
        self.assertTrue(TestParser.checkParser(input, expect, 299))
    def test_all_21(self):
        input = """

        void main(){ 
                      foo(a[a],fasf[3],aaaa[_asdasd_*1321321]);
                      babababababa;
                      int i;
                      i=aaaa;
        }

         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 300))
