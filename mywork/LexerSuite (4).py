import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
    def test_identifie2(self):
        self.assertTrue(TestLexer.checkLexeme("aCBbdc","aCBbdc,<EOF>",102))
    def test_identifier3(self):
        self.assertTrue(TestLexer.checkLexeme("true%false","true,%,false,<EOF>",103))    
    def test_identifier4(self):
        self.assertTrue(TestLexer.checkLexeme("_abc","_abc,<EOF>",104))
    def test_identifier5(self):
        self.assertTrue(TestLexer.checkLexeme("_abc_","_abc_,<EOF>",105))
    def test_identifier6(self):
        self.assertTrue(TestLexer.checkLexeme("MINHDANG123","MINHDANG123,<EOF>",106))
    def test_identifier7(self):
        self.assertTrue(TestLexer.checkLexeme("222222minhDANG123","222222,minhDANG123,<EOF>",107))    
    def test_integer1(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("00033","00033,<EOF>",108))
    def test_integer2(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("123123", "123123,<EOF>", 109))
    def test_float1(self):
        """test floatlit"""
        self.assertTrue(TestLexer.checkLexeme("1.2e-2","1.2e-2,<EOF>",110))
    def test_float2(self):
        """test floatlit"""
        self.assertTrue(TestLexer.checkLexeme("12e2.2","12e2,.2,<EOF>",111))
    def test_float3(self):
        """test floatlit"""
        self.assertTrue(TestLexer.checkLexeme("1.2e2.","1.2e2,Error Token .",112))
    def test_float4(self):
        """test floatlit"""
        self.assertTrue(TestLexer.checkLexeme("1.e-2","1.e-2,<EOF>",113))
    def test_float5(self):
        """test floatlit"""
        self.assertTrue(TestLexer.checkLexeme("1.e-2","1.e-2,<EOF>",114))
    def test_float6(self):
        """test floatlit"""
        self.assertTrue(TestLexer.checkLexeme(".123333e-2",".123333e-2,<EOF>",115))
    def test_float7(self):
        """test floatlit"""
        self.assertTrue(TestLexer.checkLexeme("1.e-32.2e123","1.e-32,.2e123,<EOF>",116))
    def test_float8(self):
        """test floatlit"""
        self.assertTrue(TestLexer.checkLexeme("1.e-2","1.e-2,<EOF>",117))
    def test_float9(self):
        """test floatlit"""
        self.assertTrue(TestLexer.checkLexeme("1.1.1.1.1.1.1","1.1,.1,.1,.1,.1,.1,<EOF>",118))
    def test_float10(self):
        """test floatlit"""
        self.assertTrue(TestLexer.checkLexeme("1.1.1.1.1.1.1.","1.1,.1,.1,.1,.1,.1,Error Token .",119))
    def test_float11(self):
        """test floatlit"""
        self.assertTrue(TestLexer.checkLexeme(".1e.1",".1,e,.1,<EOF>",120))
    def test_float12(self):
        """test floatlit"""
        self.assertTrue(TestLexer.checkLexeme("1e1.2.1e.1e-32.2","1e1,.2,.1,e,.1e-32,.2,<EOF>",121))
    def test_float13(self):
        """test floatlit"""
        self.assertTrue(TestLexer.checkLexeme("1e1.2.1e.1e-32.2","1e1,.2,.1,e,.1e-32,.2,<EOF>",122))
    def test_func_tokens(self):
        self.assertTrue(TestLexer.checkLexeme("int mark(){}","int,mark,(,),{,},<EOF>",123))
    def test_func_tokens2(self):
        self.assertTrue(TestLexer.checkLexeme("void main(){int a;}","void,main,(,),{,int,a,;,},<EOF>",124))
    def test_declare(self):
        self.assertTrue(TestLexer.checkLexeme("float a,b,c,s[5];","float,a,,,b,,,c,,,s,[,5,],;,<EOF>",125))
    def test_declare2(self):
        self.assertTrue(TestLexer.checkLexeme("float a,b;","float,a,,,b,;,<EOF>",126))
    def test_declare3(self):
        self.assertTrue(TestLexer.checkLexeme("boolean axd[2];","boolean,axd,[,2,],;,<EOF>",127))
    def test_declare4(self):
        self.assertTrue(TestLexer.checkLexeme("boolean a[b[2]];","boolean,a,[,b,[,2,],],;,<EOF>",128))
    def test_if(self):
        self.assertTrue(TestLexer.checkLexeme("if(aisd==1){return i;}","if,(,aisd,==,1,),{,return,i,;,},<EOF>",129))
    def test_if_else(self):
        self.assertTrue(TestLexer.checkLexeme("if(a==1){return i;} else {i=1;}","if,(,a,==,1,),{,return,i,;,},else,{,i,=,1,;,},<EOF>",130))
    def test_expression1(self):
        self.assertTrue(TestLexer.checkLexeme("a = A + b - 2/2","a,=,A,+,b,-,2,/,2,<EOF>",131))
    def test_expression2(self):
        self.assertTrue(TestLexer.checkLexeme("b = c[5] + i + foo(123)","b,=,c,[,5,],+,i,+,foo,(,123,),<EOF>",132))
    def test_expression3(self):
        self.assertTrue(TestLexer.checkLexeme("a>b<=c>i","a,>,b,<=,c,>,i,<EOF>",133))   
    def test_expression4(self):
        self.assertTrue(TestLexer.checkLexeme("(a+5)+cal(b+c)","(,a,+,5,),+,cal,(,b,+,c,),<EOF>",134))
    def test_expression5(self):
        self.assertTrue(TestLexer.checkLexeme("(a+5)+cal(b+c)","(,a,+,5,),+,cal,(,b,+,c,),<EOF>",135))
    def test_errortoken1(self):
        self.assertTrue(TestLexer.checkLexeme("(a+5)+cal(b+c)?","(,a,+,5,),+,cal,(,b,+,c,),Error Token ?",136))
    def test_errortoken2(self):
        self.assertTrue(TestLexer.checkLexeme("abc#","abc,Error Token #",137))
    def test_errortoken3(self):
        self.assertTrue(TestLexer.checkLexeme("a~?c#","a,Error Token ~",138))
    def test_errortoken4(self):
        self.assertTrue(TestLexer.checkLexeme("abc^","abc,Error Token ^",139))
    def test_errortoken5(self):
        self.assertTrue(TestLexer.checkLexeme("(!a=b)&&c-i?","(,!,a,=,b,),&&,c,-,i,Error Token ?",140))
    def test_errortoken6(self):
        self.assertTrue(TestLexer.checkLexeme("abc$","abc,Error Token $",141))
    def test_expression11(self):
        self.assertTrue(TestLexer.checkLexeme("float float = 2;","float,float,=,2,;,<EOF>",142))
    def test_expression22(self):
        self.assertTrue(TestLexer.checkLexeme("float float = 2;","float,float,=,2,;,<EOF>",143))
    def test_expression33(self):
        self.assertTrue(TestLexer.checkLexeme("a==b==c;","a,==,b,==,c,;,<EOF>",144))   
    def test_increment(self):
        self.assertTrue(TestLexer.checkLexeme("a++;","a,+,+,;,<EOF>",145))
    def test_decrement(self):
        self.assertTrue(TestLexer.checkLexeme("a--;","a,-,-,;,<EOF>",146))
    def test_expression7(self):
        self.assertTrue(TestLexer.checkLexeme("a<c;","a,<,c,;,<EOF>",147))
    def test_expression8(self):
        self.assertTrue(TestLexer.checkLexeme("a<=c;b=shitt;","a,<=,c,;,b,=,shitt,;,<EOF>",148) )
    def test_operator1(self):
        self.assertTrue(TestLexer.checkLexeme("+-*%!=!","+,-,*,%,!=,!,<EOF>",149))
    def test_operator2(self):
        self.assertTrue(TestLexer.checkLexeme("><>=<====",">,<,>=,<=,==,=,<EOF>",150))
    def test_comment(self):
        self.assertTrue(TestLexer.checkLexeme("//this is a comment","<EOF>",151))
    def test_comment2(self):
        self.assertTrue(TestLexer.checkLexeme("//this is a comment/*comment*/","<EOF>",152))
    def test_comment3(self):
        self.assertTrue(TestLexer.checkLexeme("/*this is a /n multiline comment*/","<EOF>",153))
    def test_comment4(self):
        self.assertTrue(TestLexer.checkLexeme("""/*this is aaaaaaaaaaaaaaaa nhieu dong comment 
            multilineeeeeeeeee commenttttttttttttttttttttttttttttttttttttttttt*/ ""","<EOF>",154))
    def test_comment5(self):
        self.assertTrue(TestLexer.checkLexeme("""/* comment 1       */ ""","<EOF>",155))
    def test_comment6(self):
        self.assertTrue(TestLexer.checkLexeme("""/*  comment 1 ep 2  1.23.214112.421 */ ""","<EOF>",156))
    def test_identifier8(self):
        self.assertTrue(TestLexer.checkLexeme("_covery_discovery12444","_covery_discovery12444,<EOF>",157))
    def test_identifier9(self):
        self.assertTrue(TestLexer.checkLexeme("123_disco_disco123","123,_disco_disco123,<EOF>",158))
    def test_identifier10(self):
        self.assertTrue(TestLexer.checkLexeme("i love you;","i,love,you,;,<EOF>",159))
    def test_string1(self):
        """test stringlit"""
        self.assertTrue(TestLexer.checkLexeme(""" "assssd\\\"tsdf" ""","""assssd\\"tsdf,<EOF>""",160))
    def test_string2(self):
        """test stringlit"""
        self.assertTrue(TestLexer.checkLexeme(""" "MINH\\\\DANG\\t\" ""","""MINH\\\\DANG\\t,<EOF>""",161))
    def test_string3(self):
        """test stringlit"""
        self.assertTrue(TestLexer.checkLexeme(""" "MINH\\bDANG\\t\" ""","""MINH\\bDANG\\t,<EOF>""",162))
    def test_string4(self):
        """test stringlit"""
        self.assertTrue(TestLexer.checkLexeme(""" "DANG MINH" ""","""DANG MINH,<EOF>""",163))
    def test_string5(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(""" "123a\\n123" ""","""123a\\n123,<EOF>""",164))
    def test_unclose_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123a\\n12""","""Unclosed String: 123a\\n12""",165))
    def test_illegal_escape(self):
        self.assertTrue(TestLexer.checkLexeme(""" 125 "123a\\m123" ""","""125,Illegal Escape In String: 123a\\m""",166))
    def test_double_slash(self):
        self.assertTrue(TestLexer.checkLexeme(""" 125 "123a\\\\125" ""","""125,123a\\\\125,<EOF>""",167))
    def test_string6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "125\\" ""","""Unclosed String: 125\\" """, 168))
    def test_string7(self):
        self.assertTrue(TestLexer.checkLexeme(""" "DANG MINH" "DANG MINH" """, """DANG MINH,DANG MINH,<EOF>""", 169))
    def test_string8(self):
        self.assertTrue(TestLexer.checkLexeme(""" "DANG\\tTri" "DANG\\0Tri" ""","""DANG\\tTri,Illegal Escape In String: DANG\\0""", 170))
    def test_string9(self):
        self.assertTrue(TestLexer.checkLexeme(""" "DANG\\tTri" "DANG\nTri" ""","""DANG\\tTri,Unclosed String: DANG""", 171))
    def test_string11(self):
        self.assertTrue(TestLexer.checkLexeme(""" "DANG\\bTri" ""","""DANG\\bTri,<EOF>""", 172))
    def test_string12(self):
        self.assertTrue(TestLexer.checkLexeme(""" "DANG\\bTri"" ""","""DANG\\bTri,Unclosed String:  """, 173))
    def test_string122(self):
        self.assertTrue(TestLexer.checkLexeme(""" "DANG\nTri"" ""","""Unclosed String: DANG""", 174))
    def test_string13(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123a\\n123" ""","""123a\\n123,<EOF>""",175))
    def test_string14(self):
        self.assertTrue(TestLexer.checkLexeme(""" 1.2e-3.2E4"abcd\\b12345" "DANGtri\\bTri" ""","""1.2e-3,.2E4,abcd\\b12345,DANGtri\\bTri,<EOF>""",176))
    def test_string15(self):
        self.assertTrue(TestLexer.checkLexeme(""" "%$%^&" ""","""%$%^&,<EOF>""",177))
    def test_string16(self):
        self.assertTrue(TestLexer.checkLexeme(""" "DANG MINH 12u%^$#" ""","""DANG MINH 12u%^$#,<EOF>""",178))
    def test_string17(self):
        self.assertTrue(TestLexer.checkLexeme(""" 125"" ""","""125,,<EOF>""",179))
    def test_string18(self):
        self.assertTrue(TestLexer.checkLexeme(""" "" """,""",<EOF>""",180))
    def test_string19(self):
        self.assertTrue(TestLexer.checkLexeme(""" abcd"" ""","""abcd,,<EOF>""",181))
    def test_string20(self):
        self.assertTrue(TestLexer.checkLexeme(""" 1234.E2abcd"" ""","""1234.E2,abcd,,<EOF>""",182))
    def test_string21(self):
        self.assertTrue(TestLexer.checkLexeme(""" abcd"DANG\\mHUng" ""","""abcd,Illegal Escape In String: DANG\\m""",183))
    def test_string22(self):
        self.assertTrue(TestLexer.checkLexeme(""" "DANG\\tTri" "DANG\\tTri" ""","""DANG\\tTri,DANG\\tTri,<EOF>""",184))
    def test_string23(self):
        self.assertTrue(TestLexer.checkLexeme(""" 125 "DANG\\tTri  ""","""125,Unclosed String: DANG\\tTri  """,185))
    def test_string24(self):
        self.assertTrue(TestLexer.checkLexeme(""" 125 "1e.245"  ""","""125,1e.245,<EOF>""",186))
    def test_string25(self):
        self.assertTrue(TestLexer.checkLexeme(""" 125 "1e.245""$%##" _abcd ""","""125,1e.245,$%##,_abcd,<EOF>""",187))
    def test_string26(self):
        self.assertTrue(TestLexer.checkLexeme(""" 125 "1e.245\\\\"  ""","""125,1e.245\\\\,<EOF>""",188))
    def test_string27(self):
        self.assertTrue(TestLexer.checkLexeme(""" 125 "1e.245""","""125,Unclosed String: 1e.245""",189))
    def test_string28(self):
        self.assertTrue(TestLexer.checkLexeme(""" 125 "1e.245??" 125.  ""","""125,1e.245??,125.,<EOF>""",190))
    def test_string29(self):
        self.assertTrue(TestLexer.checkLexeme(""" 125 "1e.245??" 125?  ""","""125,1e.245??,125,Error Token ?""",191))
    def test_string30(self):
        self.assertTrue(TestLexer.checkLexeme(""" 125 "1e.245??" 125.E23_abcde ""","""125,1e.245??,125.E23,_abcde,<EOF>""",192))
    def test_string31(self):
        self.assertTrue(TestLexer.checkLexeme(""" "DANG\\tToan||MINH\\fDANG\\\\DANG???\\tTri"  ""","""DANG\\tToan||MINH\\fDANG\\\\DANG???\\tTri,<EOF>""",193))
    def test_string32(self):
        self.assertTrue(TestLexer.checkLexeme(""" "DANG\\bToan||MINH\\bDANG\\mDANG???\\tTri"  ""","""Illegal Escape In String: DANG\\bToan||MINH\\bDANG\\m""",194))
    def test_string33(self):
        self.assertTrue(TestLexer.checkLexeme(""" "DANG\\bToan||MINH\\bDANG\\\\mDANG???\\tTri"  ""","""DANG\\bToan||MINH\\bDANG\\\\mDANG???\\tTri,<EOF>""",195))
    def test_string34(self):
        self.assertTrue(TestLexer.checkLexeme(""" "DANG\\tTri" "DANG\\0Tri" ""","""DANG\\tTri,Illegal Escape In String: DANG\\0""",196))
    def test_string35(self):
        self.assertTrue(TestLexer.checkLexeme(""" "DANG\\nTri""hello hello alo\\a" ""","""DANG\\nTri,Illegal Escape In String: hello hello alo\\a""", 197))
####################################
    def test_extra1(self):
        self.assertTrue(TestLexer.checkLexeme("/* adsafsafalfalfalsfdsadsada, ","/,*,adsafsafalfalfalsfdsadsada,,,<EOF>" ,198))
    def test_extra2(self):
        self.assertTrue(TestLexer.checkLexeme("a[[[[[[[[[10]]]]]]]]] ","a,[,[,[,[,[,[,[,[,[,10,],],],],],],],],],<EOF>" ,199))
    def test_extra3(self):        
        self.assertTrue(TestLexer.checkLexeme("a=a++++++++++++-------**** ", "a,=,a,+,+,+,+,+,+,+,+,+,+,+,+,-,-,-,-,-,-,-,*,*,*,*,<EOF>",200)) 
