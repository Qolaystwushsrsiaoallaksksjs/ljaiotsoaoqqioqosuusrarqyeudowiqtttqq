builtglob = list(globals().keys())
from argparse import ArgumentParser, Namespace
from tokenize import tokenize, untokenize, TokenInfo
from random import choice, shuffle, randint
from time import strftime
from ast import *
from re import findall
from io import BytesIO
from time import sleep
from io import StringIO 
from time import sleep
from pathlib import Path
from time import strftime   
from zlib import compress
from binascii import hexlify
from getpass import getpass
from functools import reduce
from datetime import datetime
import dis, subprocess, requests, tempfile, shutil, itertools, zipfile, re, os, sys, zlib, copy, marshal, typing, random, ast, base64, string, time, datetime
import requests
from concurrent.futures import ThreadPoolExecutor
import os
import sys
import time
from time import sleep
import nguyenthanhngoc
from nguyenthanhngoc import *
import random
import time

def clear():
    os.system("cls" if os.name == "nt" else "clear")
clear()


def clear():
    os.system("cls" if os.name == "nt" else "clear")
clear()   


print("\033[1;97m[———————[COPYRIGHT : MINHNGUYEN3004 AND NGOCVU3007]———————]")

print("\033[1;97m[—————————————————————[OBFUSCATION]———————————————————————]")

print("\033[1;97m[═════════════════════════════════════════════════════════]")



    
sleep(1)
sleep(0)
def title(start):
    while True:
        curr_time = str(datetime.timedelta(seconds = (time.time() - start))).split(".")[0]
        return curr_time

t = time.time()
rd_v1 = [1]
rd = [100,200,300,400]
class MINHNGUYEN3004_hyper:
    def __init__(self, content: str, clean = True, obfcontent = True, renlibs = True, renvars = True, addbuiltins = True, randlines = True, safemode = True, ultrasafemode = False) -> None: 
        if ultrasafemode == True:
            randlines, renlibs, renvars = False, False, False
        self.content = "exec('')\n\n" + content
        self.add_imports = []
        self.impcontent2 = []
        if addbuiltins:            
            self.AddBuiltins()        
        self.CreateVars()
        if renlibs:            
            valid = self.RenameImports()
        if renvars and valid:
            self.RenameVars()
        self.strings = {}
        if obfcontent:            
            self.ObfContent()
        if clean:            
            self.CleanCode()
        if not self._verify_lin(content):
            randlines = False
        if randlines:            
            self.RandLines()
        self.Organise()
        if clean:            
            self.CleanCode()
        else:
            self.content = ';'.join(self.content)    
    def AddBuiltins(self):
        imp = "from builtins import " + ','.join(f'{var}' for var in builtglob if not var.startswith('__') and var not in ('None', 'True', 'False') and f'{var}(' in self.content) + '\n'
        if imp == "from builtins import \n":
            imp = ""
        self.content = imp + self.content
    def CreateVars(self):
        self.globals = self._randvar()
        self.locals = self._randvar()
        self.vars = self._randvar()
        self.__import__ = self._randvar()
        imports = self._to_import
        impcontent = """
{0}()['{1}']=locals
{1}()['{2}']=__import__
{0}()['{3}']={2}('builtins').vars"""[1:].format(self.globals, self.locals, self.__import__, self.vars, self.unhexlify).splitlines()
        nimpcontent = [f"{self._randglob()}()['{imports[imp]}']={imp}" for imp in imports]
        shuffle(nimpcontent)
        impcontent.extend(iter(nimpcontent))
        self.local_import = f"locals()['{self.globals}']=globals"
        self.impcontent = impcontent       
    def RenameImports(self):
        _imports = self._gather_imports()
        if _imports == False:
            return False
        imports = []
        for imp in _imports:
            imports.extend(iter(imp))
        self.imports = {}
        for imp in imports:
            self.imports[imp] = self._randvar()
        impcontent = [f"{self._randglob()}()['{self.imports[imp]}']={self._randglob()}()[{self._protect(imp)}]" for imp in self.imports]
        shuffle(impcontent)
        self.add_imports = [lin for lin in self.content.splitlines() if self._is_valid(lin)]
        self.content = '\n'.join(lin for lin in self.content.splitlines() if lin not in self.add_imports)
        self.impcontent2 = iter(impcontent)
        return True
    def RenameVars(self):
        f = BytesIO(self.content.encode('utf-8'))
        self.tokens = list(tokenize(f.readline))
        strings = {}
        ntokens = []
        passed = []
        for token in self.tokens:
            string, type = token.string, token.type            
            if type == 1:
                if (
                    ((self.tokens[self.tokens.index(token)+1].string == '=' and self._is_not_arg(string)) or
                    self.tokens[self.tokens.index(token)-1].string in ('def', 'class')) and
                    self._check_fstring(string) and
                    self._is_not_library(token=token) and
                    string not in passed and
                    string not in self.imports and
                    (not string.startswith('__') and not string.endswith('__'))
                    ):
                    string = self._randvar()
                    strings[token.string] = string
                elif string in strings and self._is_not_library(token=token) and self.tokens[self.tokens.index(token)+1].string != '=':
                    string = strings[string]
                elif string in self.imports and self._is_exact_library(token=token):
                    if ((self.tokens[self.tokens.index(token)+1].string != '=') and
                        self.tokens[self.tokens.index(token)-1].string not in ('def', 'class')):
                        string = self.imports[string]
                else:
                    passed.append(string)            
            ntokens.append(TokenInfo(type, string, token.start, token.end, token.line))
        self.content = untokenize(ntokens).decode('utf-8') 
    def ObfContent(self):
        f = BytesIO(self.content.encode('utf-8'))
        self.tokens = list(tokenize(f.readline))
        ntokens = []
        for token in self.tokens:
            string, type = token.string, token.type
            if type == 1:
                if string in ('True', 'False'):
                    string = self._obf_bool(string)
            elif type == 2:
                string = self._obf_int(string)
            elif type == 3:
                string = self._obf_str(string)
            ntokens.append(TokenInfo(type, string, token.start, token.end, token.line))
        self.lambdas = []
        self._add_lambdas()
        strings = [f"{self.vars}()[{self._protect(var)}]={value}" for var, value in self.strings.items()]
        shuffle(strings)
        self.strings = strings
        self.content = untokenize(ntokens).decode('utf-8')
    def CleanCode(self):            
            self.RemoveComments()
            self.CompressCode()
    def RandLines(self):
        content = []
        lines = self.content.splitlines()    
        for lin, nextlin in zip(lines, range(len(lines))):
            content.append(lin)
            if (
                    nextlin == len(lines)-1 or
                    self._get_first_statement(lines[nextlin+1]) in ('elif', 'else', 'except', 'finally') or
                    lin.strip()[-1] == ','
                ):
                continue
            fakelin = self._fake_lin(self._get_indentations(lines[nextlin+1]))
            content.append(fakelin)
        self.content = '\n'.join(content)        
    def Organise(self):
        gd_vars = [f"{self.globals}()[{self._protect(self.getattr, basic=True, )}]=getattr", f"{self.globals}()[{self._protect(self.dir, basic=True)}]=dir"]
        shuffle(gd_vars)
        exec_var = f"{self.globals}()[{self._protect(self.exec)}]={self._protect_built('exec')}"
        add_imports = [f"{self.globals}()[{self._protect(self.exec)}]({self._protect(imp.strip())})" for imp in self.add_imports]
        self.content = self.local_import + '\n' + '\n'.join(gd_vars) + '\n' + '\n'.join(self.impcontent) + '\n' + exec_var + '\n' + '\n'.join(add_imports) + '\n' + '\n'.join(self.impcontent2) + '\n' + '\n'.join(self.strings) + '\n' + self.content
        return self.content
    def _verify_lin(self, content):
        return all(lin.strip() not in ['(','[','{','}',']',')'] for lin in content.splitlines())
    def _hex(self, var):
        return ''.join(f"\\x{hexlify(char.encode('utf-8')).decode('utf-8')}" for char in var)
    def _randvar(self):
        return choice((
            ''.join(choice(('失去你就像失去一個代碼塊'*random.choice(rd),'我愛你像我愛視覺代碼一樣'*random.choice(rd))) for _ in range(randint(17, 70))),
            '我愛你'* random.choice(rd) + ''.join(choice(('黑客'*random.choice(rd),'騙子'*random.choice(rd),'是一個錯誤'*random.choice(rd))) for _ in range(randint(17, 70))),
            ''.join(choice(('編碼'*random.choice(rd),'騙子'*random.choice(rd),'是一個錯誤'*random.choice(rd))) for _ in range(randint(17, 70))),
            ''.join(choice(('無法解碼'*random.choice(rd),'請尊重碼農'*random.choice(rd),'我愛你'*random.choice(rd))) for _ in range(randint(17, 70)))
        ))    
    def _randglob(self):
        return choice((
            self.globals,
            self.locals,
            self.vars
        ))
    def _protect(self, var, basic=False, r=0, char=1):
        char = "'" if char == 1 else '"'
        if basic:
            return f"{char}{''.join(reversed(var))}{char}[::+-+-(-(+1))]"
        if type(var) == int:
            return self._adv_int(var)
        if r == 0:
            r = randint(1, 2)
        if r == 1:
            return f"{self.unhexlify}({hexlify(var.encode('utf-8'))}).decode({self.utf8})"
        else:
            return f"{char}{''.join(reversed(var))}{char}[::+-+-(-(+{self._protect(1, basic=basic)}))]"
    def _protect_built(self, var, lib='builtins'):
        protected = self._protect(lib, r=2, basic=True)
        return f"{self.getattr}({self.__import__}({protected}),{self.dir}({self.__import__}({protected}))[{self.dir}({self.__import__}({protected})).index({self._protect(var, r=2, basic=True)})])"
    @property
    def _to_import(self):
        self.dir = self._randvar()
        self.getattr = self._randvar()
        self.exec = self._randvar()        
        self.eval = self._randvar()
        self.compile = self._randvar()
        self.join = self._randvar()
        self.true = self._randvar()
        self.false = self._randvar()
        self.bool = self._randvar()
        self.str = self._randvar()
        self.float = self._randvar()
        self.unhexlify = self._randvar()
        imports = {
            self._protect_built('eval'): self.eval,
            self._protect_built('compile'): self.compile,
            "''.join": self.join,
            self._protect_built('True'): self.true,
            self._protect_built('False'): self.false,
            self._protect_built('bool'): self.bool,
            self._protect_built('str'): self.str,
            self._protect_built('float'): self.float,
            self._protect_built('unhexlify', lib='binascii'): self.unhexlify,
        }
        return imports
    @property
    def utf8(self):
        return self._protect('utf8', basic=True, r=2)
    def _gather_imports(self):
        imports = [lin for lin in self.content.splitlines() if self._is_valid(lin)]
        for imp in imports:
            if '*' in imp:
                return False
        return [imp.replace('import ',',').replace('from ', '').replace(' ','').split(',')[1:] if 'from' in imp else imp.replace('import ', '').replace(' ','').split(',') for imp in imports]
    def _is_exact_library(self, token: str):
        ntoken = token
        while True:
            if self.tokens[self.tokens.index(token)-1].string == '.':
                token = self.tokens[self.tokens.index(token)-2]
            else:
                break            
        return ntoken == token    
    def _obf_bool(self, string):
        if string == 'False':
            obf = f'not({self.bool}({self.str}({self.false})))'
        elif string == 'True':
            obf = f'{self.bool}((~{self.false})or(({self.true})and({self.false})))'
        string = self._randvar()
        while string in self.strings:
            string = self._randvar()
        self.strings[string] = obf
        return string
    def _obf_int(self, string):
        if string.isdigit():
            obf = self._adv_int(int(string))
        elif string.replace('.','').isdigit():
            obf = f"{self.float}({self._protect(string)})"
        else:
            return string
        string = self._randvar()
        while string in self.strings:
            string = self._randvar()
        self.strings[string] = obf
        return string    
    def _obf_str(self, string):
        obf, do = self._adv_str(string)
        if do:
            string = self._randvar()
            while string in self.strings:
                string = self._randvar()
            self.strings[string] = obf
        else:
            string = obf
        return string
    def _adv_int(self, string):
        n = choice((1, 2))
        if n == 1:
            rnum = randint(999999999,999999999)
            x = rnum - string
            return f"{self.eval}({self._protect(f'{self._underscore_int(rnum)}+(-{self._underscore_int(x)})')})"
        elif n == 2:
            rnum = randint(0, string)
            x = string - rnum
            return f"{self.eval}({self._protect(f'{self._underscore_int(x)}-(-{self._underscore_int(rnum)})')})"    
    def _adv_str(self, string):    
        var = f"""{self.eval}({self._protect(string, r=1)})"""
        if (string.replace('b','').replace('u','').replace('r','').replace('f','')[0] == '"' and string.split('"')[0].count('f') != 0) or (string.replace('b','').replace('u','').replace('r','').replace('f','')[0] == "'" and string.split("'")[0].count('f') != 0):
            return var, False
        return var, True
    def _underscore_int(self, string):
        return '_'.join(str(string)).replace('-_','-').replace('+_','+')
    def RemoveComments(self):
        self.content = "".join(lin + '\n' for lin in self.content.splitlines() if lin.strip() and not lin.strip().startswith('#'))
    def CompressCode(self):
        content = self.content
        while True:
            for x in ('=','(',')','[',']','{','}','*','+','-','/',':','<','>',','):
                content = content.replace(f' {x}', x).replace(f'{x} ', x)
            if content == self.content:
                break
            self.content = content
    def _get_indentations(self, lin):
        i = 0
        for x in lin:
            if x == ' ':
                i += 1
            else:
                break
        return i
    def _get_first_statement(self, lin):
        s = ''
        for x in lin.strip():
            if x.lower() in 'abcxyz':
                s += x
            else:
                break
        return s    
    def _add_lambdas(self):
        for _ in range(10):
            lamb = self._randvar()
            arg = self._randvar()
            self.strings[lamb] = f'lambda {arg}:{self._randglob()}()'
            self.lambdas.append(lamb)         
def Hyper_Minh(code):
    rac = [10000]
    cre = """

"""
    copy = 'NGOCVU3007 x NguyenMinh2412'
    check_cyber = """
import os
import sys
import time
if os.name == "linux":  # OBFUSCATION : MINHNGUYEN3004 X NGOCVU3007
    os.system("clear")
elif os.name == "nt":  # BẠN ĐỪNG LÀM THẾ !
    os.system("cls")
with open(sys.argv[0], 'r') as file:
    content = file.read()
    if (_LOCATION_ != ['VIETNAM']):
        print("\033[1;97mBạn Ngu Thế Dễ Gì Đổi Đc Vienam =))")
    if (_AUTHOR_ != ['ADMIN','MINHNGUYEN3004','NGOCVU3007']):
        print("\033[1;97mBạn Ngu Thế Dễ Gì Đổi Đc Author =))")
        sys.exit(1)
    if (_PYTHON_ != ['# !/usr/bin/python3.11']):
        print("\033[1;97mBạn Ngu Thế Dễ Gì Đổi Đc Python =))")
        sys.exit(1)
    if (_PROJECT_ != ['TIGER-OBFUSCATION']):
        print("\033[1;97mBạn Ngu Thế Dễ Gì Đổi Đc Project =))")
        sys.exit(1)
import os,sys,time
a = 2
while a > 0:
    print(f'>> Loading....', end = "\\r")
    time.sleep(1)
    a -= 1        
"""
    co = check_cyber + '\n' + code # <--- cre + 
    script = co
    renvars, renlibs = False, False
    randlines = False
    Hype = MINHNGUYEN3004_hyper(content=script, renvars = renvars, renlibs = renlibs, randlines = randlines)
    a_ = Hype.Organise()
    return f"_PYTHON_ = ['# !/usr/bin/python3.11']\n_AUTHOR_ = ['ADMIN','MINHNGUYEN3004','NGOCVU3007']\n_PROJECT_ = ['TIGER-OBFUSCATION']\n_LOCATION_ = ['VIETNAM']\n" + "exec(str(chr(35) + chr(1)));"*random.choice(rac) + cre + a_
def random_string(minlength: int, maxlength: int):
    return random.choice("我氧我氧失去你就像失去一個代碼塊") + "".join(
        random.choice("0O000O0000O00O00") for _ in range(random.randint(minlength, maxlength))
    )
def obfuscate_string(s: str) -> BinOp | Call | Subscript:
    var1 = random_string(40, 40)
    var2 = random_string(40, 40)
    random_divisor = random.randint(2, 6)
    chars = list(
        filter(lambda x: ord(x) % random_divisor == 0, [chr(x) for x in range(0, 126)])
    )
    list_of_chars = "".join([random.choice(chars) for _ in range(15)])
    table0 = [
        lambda: Str(s=""),
        lambda: Call(
            func=Attribute(value=Str(s=""), attr="join", ctx=Load()),
            args=[
                Call(
                    func=Name(id="filter", ctx=Load()),
                    args=[
                        Lambda(
                            args=arguments(
                                args=[arg(arg=var1, annotation=None)],
                                vararg=None,
                                posonlyargs=[],
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=Compare(
                                left=BinOp(
                                    left=Call(
                                        func=Name(id="ord", ctx=Load()),
                                        args=[Name(id=var1, ctx=Load())],
                                        keywords=[],
                                    ),
                                    op=Mod(),
                                    right=Num(n=random_divisor),
                                ),
                                ops=[NotEq()],
                                comparators=[Num(n=0)],
                            ),
                        ),
                        Bytes(s=list_of_chars),
                    ],
                    keywords=[],
                )
            ],
            keywords=[],
        ),
    ]
    table1 = [
        lambda x: Str(s=x),
        lambda x: Call(
            func=Name(id="chr", ctx=Load()),
            args=[Num(n=ord(x))],
            keywords=[],
            starargs=None,
            kwargs=None,
        ),
    ]
    random_bytes = os.urandom(len(s))
    pair1 = random_bytes
    pair2 = bytes([x ^ y for x, y in zip(random_bytes, s.encode("utf-8"))])
    table = [
        lambda x: BinOp(
            left=Str(s=x[: len(x) // 2]), op=Add(), right=Str(s=x[len(x) // 2 :])
        ),
        lambda x: Subscript(
            value=Str(s=x[::-1]),
            slice=Slice(lower=None, upper=None, step=Num(n=-1)),
            ctx=Load(),
        ),
        lambda x: Call(
            func=Attribute(value=Str(s=""), attr="join", ctx=Load()),
            args=[
                GeneratorExp(
                    elt=Call(
                        func=Name(id="chr", ctx=Load()),
                        args=[
                            BinOp(
                                left=Name(id=var1, ctx=Load()),
                                op=BitXor(),
                                right=Name(id=var2, ctx=Load()),
                            )
                        ],
                        keywords=[],
                    ),
                    generators=[
                        comprehension(
                            target=Tuple(
                                elts=[
                                    Name(id=var2, ctx=Store()),
                                    Name(id=var1, ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id="zip", ctx=Load()),
                                args=[Bytes(s=pair1), Bytes(s=pair2)],
                                keywords=[],
                            ),
                            ifs=[],
                            is_async=0,
                        )
                    ],
                )
            ],
            keywords=[],
        ),
    ]
    table.extend([table[2]] * 2)
    if not len(s):
        return random.choice(table0)()
    if len(s) == 1:
        return random.choice(table1)(s)
    return random.choice(table)(s)
def delete_docstring(
    node: Module | ClassDef | FunctionDef,
) -> Module | ClassDef | FunctionDef:
    node.body = [
        x
        for x in node.body
        if not (isinstance(x, Expr) and isinstance(x.value, Constant))
    ]
    return node
class Obfuscator(NodeTransformer):
    def __init__(self, passes=1):
        NodeTransformer.__init__(self)
        self.namespaces: typing.List[typing.Dict[str, str]] = [
            {x: obfuscate_string(x) for x in ["__builtins__"]}
        ]
        self.binary_operators: typing.Dict[operator, str] = {}
        self.unary_operators: typing.Dict[unaryop, str] = {}
        self.passes = passes
        self.renamed = False
        self.inlvalue = False
    def push_namespace(self):
        self.namespaces.insert(0, {})
    def pop_namespace(self):
        self.namespaces.pop(0)
    @property
    def local_namespace(self):
        return self.namespaces[0]
    @property
    def global_namespace(self):
        return self.namespaces[-1]
    def obfuscate_name(self, name: str):
        new_name = random_string(40, 40)
        self.local_namespace[name] = new_name
        return new_name
    def keep_name(self, name: str):
        self.local_namespace[name] = name
        return name
    def get_name(self, name: str):
        for namespace in self.namespaces:
            if name in namespace:
                return namespace[name]
        return name
    def visit_Import(self, node) -> Assign:
        targets = []
        values = []
        for name in node.names:
            name_tokens = name.name.split(".")
            root = name_tokens[0]
            alias = name.asname or root
            targets.append(Name(id=alias, ctx=Store()))
            values.append(
                Call(
                    func=Name(id="__import__", ctx=Load()),
                    args=[Str(s=name.name)],
                    keywords=[],
                )
            )
        node = Assign(
            targets=[Tuple(elts=targets, ctx=Store())],
            value=Tuple(elts=values, ctx=Load()),
        )

        return self.generic_visit(node)
    def visit_ImportFrom(self, node):
        nodes = []
        for name in node.names:
            full_name = f"{node.module}.{name.name}"
            name_tokens = full_name.split(".")
            alias = name.asname or name.name
            nodes.append(
                Try(
                    body=[
                        Assign(
                            targets=[Name(id=alias, ctx=Store())],
                            value=reduce(
                                lambda ret, cur: Attribute(
                                    value=ret,
                                    attr=cur,
                                    ctx=Load(),
                                ),
                                name_tokens[1:],
                                Call(
                                    func=Name(id="__import__", ctx=Load()),
                                    args=[Constant(value=full_name)],
                                    keywords=[],
                                ),
                            ),
                        )
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Name(id="ImportError", ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id=alias, ctx=Store())],
                                    value=reduce(
                                        lambda ret, cur: Attribute(
                                            value=ret,
                                            attr=cur,
                                            ctx=Load(),
                                        ),
                                        name_tokens[1:],
                                        Call(
                                            func=Name(id="__import__", ctx=Load()),
                                            args=[Constant(value=node.module)],
                                            keywords=[],
                                        ),
                                    ),
                                )
                            ],
                        )
                    ],
                    orelse=[],
                    finalbody=[],
                )
            )
        return [self.generic_visit(x) for x in nodes]
    def visit_JoinedStr(self, node) -> BinOp | Call | Constant:
        def wrapNode(node: Constant | FormattedValue) -> Constant | Call:
            if isinstance(node, FormattedValue):
                if node.conversion == 115:
                    conversion_spec = "!s"
                elif node.conversion == 114:
                    conversion_spec = "!r"
                elif node.conversion == 97:
                    conversion_spec = "!a"
                else:
                    conversion_spec = ""
                if node.format_spec:
                    format_spec = ":" + node.format_spec.values[0].value
                else:
                    format_spec = ""
                return Call(
                    func=Attribute(
                        value=Constant(
                            value="{{0{}{}}}".format(conversion_spec, format_spec)
                        ),
                        attr="format",
                        ctx=Load(),
                    ),
                    args=[node.value],
                    keywords=[],
                )
            else:
                return node
        children: typing.List[Call | Constant] = list(map(wrapNode, node.values))
        node = reduce(
            lambda res, cur: BinOp(left=res, op=Add(), right=cur),
            children[1:],
            children[0],
        )
        return self.generic_visit(node)
    def visit_Str(self, node) -> Str:
        return obfuscate_string(node.s)
    def visit_NameConstant(self, node) -> NameConstant | Compare:
        if node.value is None:
            return node
        divisor = random.randint(2, 16)
        multiplicand = random.randint(4, 8)
        value = divisor * multiplicand
        if not node.value:
            value += random.randint(1, divisor - 1)
        return Compare(
            left=BinOp(left=Num(n=value), op=Mod(), right=Num(n=divisor)),
            ops=[Eq()],
            comparators=[Num(n=0)],
        )
    def visit_Num(self, node) -> Num | BinOp:
        obfus_type = random.randint(1, 3)
        if isinstance(node.n, float):
            left, right = node.n.as_integer_ratio()
            return BinOp(left=Num(left), op=Div(), right=Num(right))
        if obfus_type == 1:
            d = random.randint(2, 16)
            return BinOp(
                left=BinOp(left=Num(node.n // d), op=Mult(), right=Num(n=d)),
                op=Add(),
                right=Num(node.n % d),
            )
        elif obfus_type == 2 and node.n:
            random_num = random.getrandbits(node.n.bit_length())
            return BinOp(
                left=Num(node.n ^ random_num), op=BitXor(), right=Num(random_num)
            )
        else:
            return node
    def visit_ClassDef(self, node) -> ClassDef:
        node = delete_docstring(node)
        if not self.renamed:
            node.name = self.obfuscate_name(node.name)
        self.push_namespace()
        node = self.generic_visit(node)
        self.pop_namespace()
        return node
    def visit_Attribute(self, node) -> Attribute | Call:
        is_store_ctx = isinstance(node.ctx, Store)
        if is_store_ctx:
            prev = self.inlvalue
            self.inlvalue = True
        if not self.inlvalue:
            if isinstance(node.value, Name):
                obj = Name(id=node.value.id, ctx=Load())
            else:
                obj = node.value
            node = Call(
                func=Name(id="getattr", ctx=Load()),
                args=[obj, Str(s=node.attr)],
                keywords=[],
                starargs=None,
                kwargs=None,
            )
        node = self.generic_visit(node)
        if is_store_ctx:
            self.inlvalue = prev
        return node
    def visit_BinOp(self, node) -> BinOp | UnaryOp | Call:
        expandable = True
        is_int = True
        for candidate_node in walk(node):
            if isinstance(candidate_node, Call):
                expandable = False
        if (
            not isinstance(node.left, Num)
            or not isinstance(node.right, Num)
            or not isinstance(node.left.n, int)
            or not isinstance(node.right.n, int)
        ):
            is_int = False
        if (
            isinstance(node.op, Add)
            and random.randint(1, 10) == 1
            and expandable
            and is_int
        ):
            node = random.choice(
                [
                    BinOp(
                        left=BinOp(left=node.left, op=BitXor(), right=node.right),
                        op=Add(),
                        right=BinOp(
                            left=Num(n=2),
                            op=Mult(),
                            right=BinOp(left=node.left, op=BitAnd(), right=node.right),
                        ),
                    ),
                    BinOp(
                        left=BinOp(left=node.left, op=BitAnd(), right=node.right),
                        op=Add(),
                        right=BinOp(left=node.left, op=BitOr(), right=node.right),
                    ),
                    BinOp(
                        left=BinOp(
                            left=Num(n=2),
                            op=Mult(),
                            right=BinOp(left=node.left, op=BitOr(), right=node.right),
                        ),
                        op=Sub(),
                        right=BinOp(left=node.left, op=BitXor(), right=node.right),
                    ),
                ]
            )
        elif (
            isinstance(node.op, Sub)
            and random.randint(1, 10) == 1
            and expandable
            and is_int
        ):
            node = random.choice(
                [
                    BinOp(
                        left=BinOp(
                            left=Num(n=2),
                            op=Mult(),
                            right=BinOp(
                                left=node.left,
                                op=BitAnd(),
                                right=BinOp(
                                    left=UnaryOp(op=Invert(), operand=node.right),
                                    op=Add(),
                                    right=Num(n=1),
                                ),
                            ),
                        ),
                        op=Add(),
                        right=BinOp(
                            left=node.left,
                            op=BitXor(),
                            right=BinOp(
                                left=UnaryOp(op=Invert(), operand=node.right),
                                op=Add(),
                                right=Num(n=1),
                            ),
                        ),
                    ),
                    BinOp(
                        left=BinOp(
                            left=node.left,
                            op=BitOr(),
                            right=BinOp(
                                left=UnaryOp(op=Invert(), operand=node.right),
                                op=Add(),
                                right=Num(n=1),
                            ),
                        ),
                        op=Add(),
                        right=BinOp(
                            left=node.left,
                            op=BitAnd(),
                            right=BinOp(
                                left=UnaryOp(op=Invert(), operand=node.right),
                                op=Add(),
                                right=Num(n=1),
                            ),
                        ),
                    ),
                    BinOp(
                        left=BinOp(
                            left=Num(n=2),
                            op=Mult(),
                            right=BinOp(
                                left=node.left,
                                op=BitOr(),
                                right=BinOp(
                                    left=UnaryOp(op=Invert(), operand=node.right),
                                    op=Add(),
                                    right=Num(n=1),
                                ),
                            ),
                        ),
                        op=Sub(),
                        right=BinOp(
                            left=node.left,
                            op=BitXor(),
                            right=BinOp(
                                left=UnaryOp(op=Invert(), operand=node.right),
                                op=Add(),
                                right=Num(n=1),
                            ),
                        ),
                    ),
                ]
            )
        elif isinstance(node.op, BitOr) and random.randint(1, 10) == 1 and expandable:
            node = random.choice(
                [
                    BinOp(
                        left=BinOp(left=node.left, op=BitXor(), right=node.right),
                        op=BitOr(),
                        right=BinOp(left=node.left, op=BitAnd(), right=node.right),
                    ),
                    UnaryOp(
                        op=Invert(),
                        operand=BinOp(
                            left=UnaryOp(
                                op=Invert(),
                                operand=BinOp(
                                    left=node.left, op=BitAnd(), right=node.left
                                ),
                            ),
                            op=BitAnd(),
                            right=UnaryOp(
                                op=Invert(),
                                operand=BinOp(
                                    left=node.right, op=BitAnd(), right=node.right
                                ),
                            ),
                        ),
                    ),
                ]
            )
        elif isinstance(node.op, BitAnd) and random.randint(1, 10) == 1 and expandable:
            node = random.choice(
                [
                    BinOp(
                        left=BinOp(left=node.left, op=BitOr(), right=node.right),
                        op=Sub(),
                        right=BinOp(left=node.left, op=BitXor(), right=node.right),
                    ),
                    UnaryOp(
                        op=Invert(),
                        operand=BinOp(
                            left=UnaryOp(
                                op=Invert(),
                                operand=BinOp(
                                    left=node.left, op=BitAnd(), right=node.right
                                ),
                            ),
                            op=BitAnd(),
                            right=UnaryOp(
                                op=Invert(),
                                operand=BinOp(
                                    left=node.left, op=BitAnd(), right=node.right
                                ),
                            ),
                        ),
                    ),
                ]
            )
        elif isinstance(node.op, BitXor) and random.randint(1, 10) == 1 and expandable:
            node = random.choice(
                [
                    BinOp(
                        left=BinOp(left=node.left, op=Sub(), right=node.right),
                        op=Add(),
                        right=BinOp(
                            left=Num(n=2),
                            op=Mult(),
                            right=BinOp(
                                left=UnaryOp(op=Invert(), operand=node.left),
                                op=BitAnd(),
                                right=node.right,
                            ),
                        ),
                    ),
                    BinOp(
                        left=UnaryOp(
                            op=Invert(),
                            operand=BinOp(
                                left=node.left, op=BitAnd(), right=node.right
                            ),
                        ),
                        op=BitAnd(),
                        right=UnaryOp(
                            op=Invert(),
                            operand=BinOp(
                                left=UnaryOp(op=Invert(), operand=node.left),
                                op=BitAnd(),
                                right=UnaryOp(op=Invert(), operand=node.right),
                            ),
                        ),
                    ),
                    BinOp(
                        left=BinOp(
                            left=UnaryOp(op=Invert(), operand=node.left),
                            op=BitAnd(),
                            right=node.right,
                        ),
                        op=BitOr(),
                        right=BinOp(
                            left=node.left,
                            op=BitAnd(),
                            right=UnaryOp(op=Invert(), operand=node.right),
                        ),
                    ),
                    BinOp(
                        left=BinOp(
                            left=node.left,
                            op=BitOr(),
                            right=node.right,
                        ),
                        op=BitAnd(),
                        right=UnaryOp(
                            op=Invert(),
                            operand=BinOp(
                                left=node.left,
                                op=BitAnd(),
                                right=node.right,
                            ),
                        ),
                    ),
                ]
            )
        else:
            try:
                if type(node.op) not in self.binary_operators:
                    new_name = random_string(40, 40)
                    self.binary_operators[type(node.op)] = new_name
                if random.randint(1, 4) == 1:
                    name = self.binary_operators[type(node.op)]
                    node = Call(
                        func=Name(name, ctx=Load()),
                        args=[node.left, node.right],
                        keywords=[],
                    )
            except:
                pass
        return self.generic_visit(node)
    def visit_UnaryOp(self, node) -> UnaryOp | Call:
        try:
            if type(node.op) not in self.unary_operators:
                new_name = random_string(40, 40)
                self.unary_operators[type(node.op)] = new_name
            if random.randint(1, 2) == 1:
                name = self.unary_operators[type(node.op)]
                node = Call(
                    func=Name(name, ctx=Load()),
                    args=[node.operand],
                    keywords=[],
                )
        except:
            pass
        return self.generic_visit(node)
    def visit_AugAssign(self, node) -> Assign:
        if isinstance(node.target, Name):
            node = Assign(
                targets=[Name(node.target.id, ctx=Store())],
                value=BinOp(
                    left=Name(node.target.id, ctx=Load()),
                    op=node.op,
                    right=node.value,
                ),
            )
        else:
            attribute = node.target
            store_attribute = copy.deepcopy(attribute)
            store_attribute.ctx = Store()
            store_attribute.value.ctx = Load()
            load_attribute = copy.deepcopy(attribute)
            load_attribute.ctx = Load()
            load_attribute.value.ctx = Load()
            node = Assign(
                targets=[store_attribute],
                value=BinOp(left=load_attribute, op=node.op, right=node.value),
            )
        return self.generic_visit(node)
    def visit_AnnAssign(self, node) -> AnnAssign:
        node.annotation = NameConstant(value=None)
        return self.generic_visit(node)
    def visit_AsyncFunctionDef(self, node) -> AsyncFunctionDef:
        return self.visit_FunctionDef(node)
    def visit_FunctionDef(self, node) -> FunctionDef:
        node = delete_docstring(node)
        no_obfuscate = "ast_no_obfuscate" in [arg.arg for arg in node.args.kwonlyargs]
        if not self.renamed:
            if no_obfuscate or (
                node.name.startswith("__") and node.name.endswith("__")
            ):
                node.name = self.keep_name(node.name)
            else:
                node.name = self.obfuscate_name(node.name)
        self.push_namespace()
        if not self.renamed:
            if no_obfuscate:
                node.args.kwonlyargs = list(
                    filter(
                        lambda arg: arg.arg != "ast_no_obfuscate", node.args.kwonlyargs
                    )
                )
            name_transformer = self.keep_name if no_obfuscate else self.obfuscate_name
            for arg in node.args.args:
                arg.arg = name_transformer(arg.arg)
                arg.annotation = NameConstant(value=None)
        node.returns = NameConstant(value=None)
        node = self.generic_visit(node)
        self.pop_namespace()
        return node
    def visit_Lambda(self, node) -> Lambda:
        no_obfuscate = "ast_no_obfuscate" in [arg.arg for arg in node.args.kwonlyargs]
        self.push_namespace()
        if not self.renamed:
            if no_obfuscate:
                node.args.kwonlyargs = list(
                    filter(
                        lambda arg: arg.arg != "ast_no_obfuscate", node.args.kwonlyargs
                    )
                )
            name_transformer = self.keep_name if no_obfuscate else self.obfuscate_name
            for arg in node.args.args:
                arg.arg = name_transformer(arg.arg)
        node = self.generic_visit(node)
        self.pop_namespace()
        return node
    def visit_Name(self, node) -> Name:
        if (
            not self.renamed
            and isinstance(node.ctx, Store)
            and node.id not in self.local_namespace
        ):
            node.id = self.obfuscate_name(node.id)
        node.id = self.get_name(node.id)
        return self.generic_visit(node)
    def visit_Module(self, node) -> Module:
        node = delete_docstring(node)
        for _ in range(self.passes):
            node = self.generic_visit(node)
            self.renamed = True
        for operator, new_name in self.binary_operators.items():
            arg1 = random_string(40, 40)
            arg2 = random_string(40, 40)
            node.body.insert(
                0,
                Assign(
                    targets=[Name(id=new_name, ctx=Store())],
                    value=Lambda(
                        args=arguments(
                            args=[
                                arg(arg=arg1, annotation=None),
                                arg(arg=arg2, annotation=None),
                            ],
                            vararg=None,
                            posonlyargs=[],
                            kwonlyargs=[],
                            kw_defaults=[],
                            kwarg=None,
                            defaults=[],
                        ),
                        body=BinOp(
                            left=Name(id=arg1, ctx=Load()),
                            op=operator(),
                            right=Name(id=arg2, ctx=Load()),
                        ),
                    ),
                ),
            )
        for operator, new_name in self.unary_operators.items():
            arg1 = random_string(40, 40)
            node.body.insert(
                0,
                Assign(
                    targets=[Name(id=new_name, ctx=Store())],
                    value=Lambda(
                        args=arguments(
                            args=[arg(arg=arg1, annotation=None)],
                            vararg=None,
                            posonlyargs=[],
                            kwonlyargs=[],
                            kw_defaults=[],
                            kwarg=None,
                            defaults=[],
                        ),
                        body=UnaryOp(operand=Name(arg1, ctx=Load()), op=operator()),
                    ),
                ),
            )
        return fix_missing_locations(node)
def Random_class_Minh(code):
    newcode = "\n"
    classes = ["沉默就像就像失就的沉默就像就像失就的".join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(67)) for i in range(67)]
    for i in classes:
        newcode += f"class {i}:\n    def __init__(self):\n"
        funcs = ["失去你就像失去一個代碼塊失失去你就像失去一個代碼塊失"+"失就像失去失就像失去" + "我愛你像我愛視覺代碼一樣我愛你像我愛視覺代碼一樣" + "失去你就像失去一個代碼塊失去你就像失去一個代碼塊" +"O0O00OO0O00O".join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(67)) for i in range(67)]
        for i in funcs:
            newcode += f"        self.{i}()\n"
        for i in funcs:
            newcode += f"    def {i}(self, {', '.join([''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(40, 67))) for i in range(random.randint(40, 67))])}):\n        return self.{random.choice(funcs)}()\n"
    newcode += code + "\n"
    classes = ["去就失失一就像個塊去就失失一就像個塊" + "失就像失去失就像失去" + "我愛你像我愛視覺代碼一樣我愛你像我愛視覺代碼一樣" + "失去你就像失去一個代碼塊失去你就像失去一個代碼塊" + "0O00O00O00O0".join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(67)) for i in range(67)] 
    for i in classes:
        newcode += f"class {i}:\n    def __init__(self):\n"
        funcs = ["去失就像一就像就像塊去失就像一就像就像塊"+"失就像失去失就像失去" + "我愛你像我愛視覺代碼一樣我愛你像我愛視覺代碼一樣" + "失去你就像失去一個代碼塊失去你就像失去一個代碼塊" + "00O0O00O0O".join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(67)) for i in range(67)]
        for i in funcs:
            newcode += f"        self.{i}()\n"
        for i in funcs:
            newcode += f"    def {i}(self, {', '.join([''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(30, 60))) for i in range(random.randint(30, 60))])}):\n        return self.{random.choice(funcs)}()\n"
    return newcode    
import time
import random
import string
import zlib
import base64
import marshal
import os

def Marshal_Minh(code):
    source_code = code.encode()
    mrs = compile(source_code, 'MINHNGUYEN3004', 'exec')
    compressed_code = zlib.compress(marshal.dumps(mrs))
    encoded_code = base64.b85encode(compressed_code)
    return f"\nexec(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b85decode(b'" + encoded_code.decode('utf-8')[::-1] + "'[::-1]))),globals())"

def Random_filename():
    return f"obf-{''.join(random.choices(string.digits, k=10))}.py"

def obf_medium(input_file):
    try:
        output_file = Random_filename()

        # Read code from the input file
        with open(input_file, 'r') as file:
            code_nay = file.read()

        print("[FILE RECEIVED! WAITING.... (5 - 360 SEC)]")
        start = time.time()

        # Obfuscate code
        class_1 = Random_class_Minh(code_nay)
        class_2 = Hyper_Minh(class_1)
        class_3 = Random_class_Minh(class_2)
        class_4 = Marshal_Minh(class_3)

        # Update obfuscation details
        obfuscation_details = {
            "_DATE_": time.strftime("%H:%M:%S','%d/%m/%Y','(UTC)"),
            "_MODE_": 'PYTHON3.11 - MEDIUM'
        }

        # Include obfuscation details in the obfuscated file
        obfuscated_code = (f"_PYTHON_ = ['# !/usr/bin/python3.11']\n"
                           f"_AUTHOR_ = ['ADMIN','MINHNGUYEN3004','NGOCVU3007']\n"
                           f"_DATE_ = ['{obfuscation_details['_DATE_']}']\n"
                           f"_MODE_ = ['{obfuscation_details['_MODE_']}']\n"
                           f"_PROJECT_ = ['TIGER-OBFUSCATION']\n"
                           f"_LOCATION_ = ['VIETNAM']{class_4}")

        print("[FILE OBFUSCATION DONE...!]")

        # Save the obfuscated code to the specified output file


# Đường dẫn đến thư mục gốc
        base_folder_path = '/storage/emulated/0/Download/bot_temp/'

# Tạo tên thư mục ngẫu nhiên
        new_folder_path = os.path.join(base_folder_path, '1')
        
# Tạo tên file ngẫu nhiên
        random_file_number = random.randint(1000000000, 9999999999)
        file_name = f'obf-{random_file_number}.py'
        full_path = os.path.join(new_folder_path, file_name)

# Đảm bảo thư mục mới tồn tại
        os.makedirs(new_folder_path, exist_ok=True)

# Ghi dữ liệu vào file
        with open(full_path, 'w', encoding='utf-8') as file:
            file.write(obfuscated_code)

        print(f"File saved at: {full_path}")


        print(f"File saved at: {full_path}")
        
        print(f"[FILE SAVED AS {output_file}]")
        print(f"[File OBFUSCATION DONE IN {round(time.time() - start)}s]")
        print("[NHỚ TEST LẠI FILE SAU KHI OBF NHÉ]")
        print("[NẾU GẶP LỖI DO OBF HÃY THỬ OBF LẠI 1-2 LẦN NHÉ]")
        print("[OBF TRÊN 10MB NHÉ ĐỪNG CÓ LÍ DO LÀ BOTNET VÌ NÓ NHIỀU LỚP BẢO MẬT KHÔNG TINTHÌ TÙY BẠN NHÉ]")
        print("[THANKS FOR USING]")
    except Exception as e:
        print(f"ERROR: {e}")

def print_banner(directory_path):
    # In thông báo


    # Lấy danh sách các file trong thư mục
    try:
        files = os.listdir(directory_path)
        file_count = 0  # Đếm số lượng file đã in trên dòng hiện tại

        # In danh sách các file
        for file in files:
            if os.path.isfile(os.path.join(directory_path, file)):
                print(f"\033[97m\033[97m[ \033[97m\033[97m{file}\033[97m\033[97m ]", end=" ")
                file_count += 1
                if file_count % 3 == 0:
                    print()  # Xuống dòng sau mỗi 3 file

        # Nếu có file còn lại sau vòng lặp
        if file_count % 3 != 0:
            print()

    except FileNotFoundError:
        print("\033[97m[════════════════════════════════════════════════════════]\033[97m")
        print("\033[97m║ Error : Thư mục không tồn tại !")
        print("\033[97m[════════════════════════════════════════════════════════]\033[97m")

    print("\033[97m[═════════════════════════════════════════════════════════]\033[97m")
    

# Thay đổi đường dẫn nếu cần, hoặc sử dụng thư mục hiện tại
current_directory = os.getcwd()
print_banner(current_directory)
# Example usage
input_file = input('\033[1;97m[NHẬP FILE] :\033[1;97m ')
obf_medium(input_file)
