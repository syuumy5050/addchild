from firebase import Firebase

firebase = Firebase()

# 定義
def print_flag():
    data = firebase.get('data/flag')
    data = 'flag : ' + str(data)
    return data

def print_message():
    data = firebase.get('data/message')
    data = 'message : ' + str(data)
    return data

def update(key, value, path):
    updates = {key : value}
    firebase.update(updates, path)


# 実際の操作表示
print('''
    ==================================================
    データベース要素追加ツール
    このツールはプロジェクトのデータベースにおける、
    フラグとメッセージを追加,削除するツールです。
    以下の指示に従って入力して下さい。''')

while True:
    print("\n")
    print(print_flag())
    print(print_message())

    print(""" 　    
    >フラグを扱う　　：f
    >メッセージを扱う：m
    >操作を終える　　：q    
    """)

    mode = input('>> ')


    #フラグ操作
    if mode == 'f':
        print(print_flag())

        print(""" 
    >要素を追加する　：a
    >要素を削除する　：d
        """)

        submode = input('>> ')

        if submode == 'a':
            print('\n追加したいフラグ名を入力して下さい')
            key = input('>> ')            

            update(key, 0, 'data/flag')

        elif submode == 'd':
            print('\n削除したいフラグ名を入力して下さい')
            key = input('>> ')            

            firebase.delete(key, "data/flag")

        else:
            print('入力された文字に間違いがあります')


    #メッセージ操作
    elif mode == 'm':
        print(print_message())

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

            update(key, val, "data/message")

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