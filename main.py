from firebase import Firebase

firebase = Firebase()

# 定義
def get_data(type):
    data = firebase.get(f"magio/{type}")
    return f"{type}: {data}"


# 実際の操作表示
print('''
    ==================================================
    データベース要素追加ツール
    ==================================================

    このツールはプロジェクトのデータベースにおける、
    フラグとメッセージを追加,削除するツールです。
    以下の指示に従って入力して下さい。''')

while True:
    print("\n")
    print(get_data("flag"))
    print(get_data("message"))

    print(""" 　    
    >フラグを扱う　　：f
    >メッセージを扱う：m
    >操作を終える　　：q    
    """)

    mode = input('>> ')


    #フラグ操作
    if mode == 'f':
        print(get_data("flag"))

        print(""" 
    >要素を追加する　：a
    >要素を削除する　：d
        """)

        submode = input('>> ')

        if submode == 'a':
            print('\n追加したいフラグ名を入力して下さい')
            key = input('>> ')            

            firebase.update({key: 0}, 'magio/flag')

        elif submode == 'd':
            print('\n削除したいフラグ名を入力して下さい')
            key = input('>> ')            

            firebase.delete(key, "data/flag")

        else:
            print('入力された文字に間違いがあります')


    #メッセージ操作
    elif mode == 'm':
        print(get_data("message"))

        print(""" 
    >要素を追加,変更する　：a
    >要素を削除する 　　　：d
        """)

        submode = input('>> ')

        if submode == 'a':
            print('\n追加,変更したいメッセージのkey名を入力して下さい')
            key = input('>> ')

            print('\nメッセージを入力して下さい')
            val = input('>> ')

            firebase.update({key: val}, 'magio/message')

        elif submode == 'd':
            print('\n削除したいメッセージのkeyを入力して下さい')
            key = input('>> ')            

            firebase.delete(key, 'data/message')

        else:
            print('入力された文字に間違いがあります')


    #その他
    elif mode == 'q':    
        break
    else:
        print('\n')
        print('入力された文字に間違いがあります')