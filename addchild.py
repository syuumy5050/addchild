from firebase import Firebase

firebase = Firebase()

# 定義
def print_data():
    print('\n')
    data = firebase.get(address)
    print(data)

def function(val):
    child = address + '/' + key

    updates = {child : val}
    firebase.update(updates)

def wrong():
    print('\n')
    print('入力された文字に間違いがあります')



# 実際の操作表示
print('''
    ==================================================
    データベース要素追加ツール
    ==================================================

    このツールはプロジェクトのデータベースにおける、
    フラグとメッセージを追加,削除するツールです。
    以下の指示に従って入力して下さい。
''')

while True:
    address = 'data'

    print_data()

    print(""" 　    
    >フラグを扱う　　：f
    >メッセージを扱う：m
    >操作を終える　　：q    
    """)

    mode = input('>> ')


    if mode == 'f':
        address += '/flag'

        print_data()

        print(""" 
    >要素を追加する　：a
    >要素を削除する　：d
        """)

        submode = input('>> ')

        if submode == 'a':
            print('\n追加したいフラグ名を入力して下さい')
            key = input('>> ')            

            function(0)

        elif submode == 'd':
            print('\n削除したいフラグ名を入力して下さい')
            key = input('>> ')            

            function({})

        else:
            wrong()
            
        print_data()

    elif mode == 'm':
        address += '/message'

        print_data()

        print(""" 
    >要素を追加,変更する　：a
    >要素を削除する 　　　：d
        """)

        submode = input('>> ')

        if submode == 'a':
            print('\n追加,変更したいメッセージのkeyを入力して下さい')
            key = input('>> ')

            print('\nメッセージを入力して下さい')
            value = input('>> ')

            function(value)

        elif submode == 'd':
            print('\n削除したいメッセージのkeyを入力して下さい')
            key = input('>> ')            

            function({})

        else:
            wrong()
            
        print_data()

    elif mode == 'q':    
        break
    else:
        wrong()