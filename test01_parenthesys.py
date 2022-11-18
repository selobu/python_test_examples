# coding: utf-8
text1 = "sin(x)+23"
text2 = "{[], sum([1,2,3])}"
text3 = "(()))"


def test_check1(param: str) -> bool:
    """Prueba inicial para verificar la cantidad de paréntesis

    Args:
        param (str): cadena de caracteres con la expresión matemática

    Returns:
        bool: True|False dependiendo de la cantidad de paréntesis
    """
    return len(param.split("(")) == len(param.split(")"))


def check(param: str) -> bool:
    """Verifica la sintaxis

    Args:
        param (str): cadena de caracteres con la expresión matemática a verificar

    Returns:
        bool: Indica si se encuentra bien escrito
    """
    match = {"(": ")", "[": "]", "{": "}"}
    res = []
    try:
        for i in param:
            if i in match.keys():
                res.append(i)
            elif i in match.values():
                v = res.pop(-1)
                if i != match[v]:
                    return False
    except IndexError:
        return False
    if len(res) == 0:
        return True
    return False


print(f"1) {text1} => {check(text1)}")  # print True
print(f"2) {text2} => {check(text2)}")  # print True
print(f"3) {text3} => {check(text3)}")  # print False
