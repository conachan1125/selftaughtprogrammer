import re
text = """
キリンは大昔から__複数名詞__の興味の対象でした。キリンは__複数名詞__のなかで
一番背が高いですが、科学者たちはそのような長い__体の一部__をどうやって獲得したのか説明出来ません。
キリンの身長は__数値__ __単位__近くあり、その高さのほとんどは足と__体の一部__によるものです
"""

def mad_libs(mls):
    """
    :param mls: 文字列で、ユーザーに入力して欲しい単語の部分はあとを2つのアンダースコアで挟んでください
    ヒントの単語にはアンダースコアを含めないでください
    __hint_hint__はダメです
    __hint__はOKです
    """
    hints = re.findall("__.*?__", mls)
    if hints is not None:
        for word in hints:
            print(mls)
            q = "{} を入力".format(word)
            new = input(q)
            mls = mls.replace(word, new, 1)
        print("\n")
        mls = mls.replace("\n", "")
        print(mls)
    else:
        print("引数mlsが無効です")

mad_libs(text)
