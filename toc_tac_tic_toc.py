import webbrowser
import random
win = False
turns = 0


#title start
text = "BROCCOLI VS BUGS"
from PIL import Image, ImageDraw, ImageFont
import numpy as np
myfont = ImageFont.truetype("verdanab.ttf", 12)
size = myfont.getsize(text)
img = Image.new("1",size,"black")
draw = ImageDraw.Draw(img)
draw.text((0, 0), text, "white", font=myfont)
pixels = np.array(img, dtype=np.uint8)
chars = np.array([' ','#'], dtype="U1")[pixels]
strings = chars.view('U' + str(chars.shape[1])).flatten()
print( "\n".join(strings))
#title end

def getnumber(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp) 
        else:
            print("NO BAD THATS NOT A NUMBER WHAT ARE YOU DOING????????????????????????????????????????")
            text = ">:("
            from PIL import Image, ImageDraw, ImageFont
            import numpy as np
            myfont = ImageFont.truetype("verdanab.ttf", 50)
            size = myfont.getsize(text)
            img = Image.new("1",size,"black")
            draw = ImageDraw.Draw(img)
            draw.text((0, 0), text, "white", font=myfont)
            pixels = np.array(img, dtype=np.uint8)
            chars = np.array([' ','#'], dtype="U1")[pixels]
            strings = chars.view('U' + str(chars.shape[1])).flatten()
            print( "\n".join(strings)) 


print("lets play toc_tac_tic_toc_tac+top_tok_toa_toq_tow_toy_tor_tou_toi_tji_tfp_teep_toc_eut_toc_toz_tox_toq_tov_tob_tob_toic_toix_toix_tos_tow_tos_tok_tol_toy_toui_dsjs_tyod_rjdkfhgf_fdjhfduk_i_give_up_loooooooong_omg_secretmessage_youwin1fronchfry_eeeeeeeee_thea_aaa")
board=[]
def printboard():
    for x in range (3):
        print(board[x])
for x in range (3):
    row = []
    for x in range (3):
        row.append("🌽")
  
    
    
    board.append(row)
    print(row)
print("start :)")
while win == False:
    
    print("you are playing as 🥦")
    x = getnumber("give me a row")
    y = getnumber("now a column plsssssssssssssssssssssssssss ╰(*°▽°*)╯")
    #webbrowser.open("https://pics.me.me/playing-tic-tac-toe-fact-44007434.png")
    turns += 1
    while x >= 3 or y >= 3 or x < 0 or y < 0 or board[x][y] != "🌽":
        print("no!!! choose again >:((")
        x = getnumber("give me a row")
        y = getnumber ("now a column plsssssssssssssssssssssssssss ╰(*°▽°*)╯")
    board[x][y] = "🥦"
    printboard()
    if turns == 9:
        webbrowser.open("https://i.stack.imgur.com/gGJEY.png")
        print("A tie, ur bad")
        break
    for x in range (3):
        if board[x][0] == "🥦" and board[x][1] == "🥦" and board[x][2] == "🥦":
            text = "BROCCOLI WINS"
            from PIL import Image, ImageDraw, ImageFont
            import numpy as np
            myfont = ImageFont.truetype("verdanab.ttf", 12)
            size = myfont.getsize(text)
            img = Image.new("1",size,"black")
            draw = ImageDraw.Draw(img)
            draw.text((0, 0), text, "white", font=myfont)
            pixels = np.array(img, dtype=np.uint8)
            chars = np.array([' ','#'], dtype="U1")[pixels]
            strings = chars.view('U' + str(chars.shape[1])).flatten()
            print( "\n".join(strings)) 
            win = True
    if win == True:
        break
    if board[1][y] == "🥦" and board[2][y] == "🥦" and board[0][y] == "🥦":
            text = "BROCCOLI WINS"
            from PIL import Image, ImageDraw, ImageFont
            import numpy as np
            myfont = ImageFont.truetype("verdanab.ttf", 12)
            size = myfont.getsize(text)
            img = Image.new("1",size,"black")
            draw = ImageDraw.Draw(img)
            draw.text((0, 0), text, "white", font=myfont)
            pixels = np.array(img, dtype=np.uint8)
            chars = np.array([' ','#'], dtype="U1")[pixels]
            strings = chars.view('U' + str(chars.shape[1])).flatten()
            print( "\n".join(strings)) 
            win = True
    if win == True:
        break
    if board[0][0] == "🥦" and board[1][1] == "🥦" and board[2][2] == "🥦":
            text = "BROCCOLI WINS"
            from PIL import Image, ImageDraw, ImageFont
            import numpy as np
            myfont = ImageFont.truetype("verdanab.ttf", 12)
            size = myfont.getsize(text)
            img = Image.new("1",size,"black")
            draw = ImageDraw.Draw(img)
            draw.text((0, 0), text, "white", font=myfont)
            pixels = np.array(img, dtype=np.uint8)
            chars = np.array([' ','#'], dtype="U1")[pixels]
            strings = chars.view('U' + str(chars.shape[1])).flatten()
            print( "\n".join(strings))   
            win = True
    if win == True:
        break
    if board[0][2] == "🥦" and board[1][1] == "🥦" and board[2][0] == "🥦":
            text = "BROCCOLI WINS"
            from PIL import Image, ImageDraw, ImageFont
            import numpy as np
            myfont = ImageFont.truetype("verdanab.ttf", 12)
            size = myfont.getsize(text)
            img = Image.new("1",size,"black")
            draw = ImageDraw.Draw(img)
            draw.text((0, 0), text, "white", font=myfont)
            pixels = np.array(img, dtype=np.uint8)
            chars = np.array([' ','#'], dtype="U1")[pixels]
            strings = chars.view('U' + str(chars.shape[1])).flatten()
            print( "\n".join(strings))  
            win = True
    if win == True:
        break
    
    print("ok now for player 2!!! :DDD (^///^)(❁´◡`❁)(^///^):-D")
    print("you are 🐛")
    o = getnumber("give me a rowww")
    b = getnumber("now a column OwO")
    turns += 1
    #webbrowser.open("https://i.redd.it/l2aifjtojx261.jpg")
    while o >= 3 or b >= 3 or o < 0 or b < 0 or board[o][b] != "🌽":
        print("no!!! choose again!!!")
        o = getnumber("give me a rowww")
        b = getnumber("now a column OwO")
    board[o][b] = "🐛"
    printboard()
    if turns == 9:
        break
    for o in range (3):
        if board[o][0] == "🐛" and board[o][1] == "🐛" and board[o][2] == "🐛":
            text = "BUGS WIN"
            from PIL import Image, ImageDraw, ImageFont
            import numpy as np
            myfont = ImageFont.truetype("verdanab.ttf", 12)
            size = myfont.getsize(text)
            img = Image.new("1",size,"black")
            draw = ImageDraw.Draw(img)
            draw.text((0, 0), text, "white", font=myfont)
            pixels = np.array(img, dtype=np.uint8)
            chars = np.array([' ','#'], dtype="U1")[pixels]
            strings = chars.view('U' + str(chars.shape[1])).flatten()
            print( "\n".join(strings)) 
            win = True
    if win == True:
        break
    if board[0][b] == "🐛" and board[1][b] == "🐛" and board[2][b] == "🐛":
            text = "BUGS WIN"
            from PIL import Image, ImageDraw, ImageFont
            import numpy as np
            myfont = ImageFont.truetype("verdanab.ttf", 12)
            size = myfont.getsize(text)
            img = Image.new("1",size,"black")
            draw = ImageDraw.Draw(img)
            draw.text((0, 0), text, "white", font=myfont)
            pixels = np.array(img, dtype=np.uint8)
            chars = np.array([' ','#'], dtype="U1")[pixels]
            strings = chars.view('U' + str(chars.shape[1])).flatten()
            print( "\n".join(strings))    
            win = True
    if win == True:
        break
    if board[0][0] == "🐛" and board[1][1] == "🐛" and board[2][2] == "🐛":
            text = "BUGS WIN"
            from PIL import Image, ImageDraw, ImageFont
            import numpy as np
            myfont = ImageFont.truetype("verdanab.ttf", 12)
            size = myfont.getsize(text)
            img = Image.new("1",size,"black")
            draw = ImageDraw.Draw(img)
            draw.text((0, 0), text, "white", font=myfont)
            pixels = np.array(img, dtype=np.uint8)
            chars = np.array([' ','#'], dtype="U1")[pixels]
            strings = chars.view('U' + str(chars.shape[1])).flatten()
            print( "\n".join(strings))    
            win = True
    if win == True:
        break
    if board[0][2] == "🐛" and board[1][1] == "🐛" and board[2][0] == "🐛":
            text = "BUGS WIN"
            from PIL import Image, ImageDraw, ImageFont
            import numpy as np
            myfont = ImageFont.truetype("verdanab.ttf", 12)
            size = myfont.getsize(text)
            img = Image.new("1",size,"black")
            draw = ImageDraw.Draw(img)
            draw.text((0, 0), text, "white", font=myfont)
            pixels = np.array(img, dtype=np.uint8)
            chars = np.array([' ','#'], dtype="U1")[pixels]
            strings = chars.view('U' + str(chars.shape[1])).flatten()
            print( "\n".join(strings))    
            win = True
    if win == True:
        break
    

links = ["https://cdn.vox-cdn.com/thumbor/L7Fd3_q_gWJBXkEtSfOBA06jD-Q=/1400x0/filters:no_upscale()/cdn.vox-cdn.com/uploads/chorus_asset/file/22522623/2hf8jy.jpg", 
"https://i.pinimg.com/originals/43/1a/36/431a3687372ea8206bc0fd5bd431c6f7.jpg",
"https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/c728a8b5-e8c0-45e5-8848-6909b9531b6c/dbtxjoh-805dbc11-dd8e-4cc7-bb41-c40954a24d50.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2M3MjhhOGI1LWU4YzAtNDVlNS04ODQ4LTY5MDliOTUzMWI2Y1wvZGJ0eGpvaC04MDVkYmMxMS1kZDhlLTRjYzctYmI0MS1jNDA5NTRhMjRkNTAucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.vhL0OGoOzPvO84UQe9yFRc7LCnlxOfEcZOWEWQitSfQ0",
"https://pics.me.me/tic-tac-toe-yall-wanna-do-tictactoe-39799991.png"
"https://media.discordapp.net/attachments/605800920579702967/866756755919863828/Tumblr_l_49763893005874.jpg",
"https://miro.medium.com/max/1400/0*z1mm6izqSeDiKukb",
"https://cdn.ebaumsworld.com/mediaFiles/picture/516050/85968924.png",
"https://vincentdnl.com/static/d39b503cebf83760d389b29b8c66d03b/6a068/semicolon2.jpg",
"https://static1.thegamerimages.com/wordpress/wp-content/uploads/2018/04/shrek-meme-3.jpg",
"https://www.syfy.com/sites/syfy/files/2021/06/shrekfest-shrek-super-slam.png",
"https://i.imgflip.com/4cd0gr.jpg",
"https://static.fandomspot.com/images/11/10388/071-shrek-shronk-meme.jpg",
"https://static3.srcdn.com/wordpress/wp-content/uploads/2019/04/1.shrek-clothes.jpg?q=50&fit=crop&w=740&h=526&dpr=1.5"
"https://www.kidscodecs.com/wp-content/uploads/2020/02/History_TS_ProgrammingMemes_image4.png",
"https://memezila.com/wp-content/Code-comments-be-like-this-is-a-stop-sign-meme-1022.png",
"https://s3.memeshappen.com/memes/Coding-Debugging.jpg",
"https://www.humanesociety.org/sites/default/files/styles/768x326/public/2018/08/freckles-horse-duchess_0.jpg?h=c47c9ce1&itok=AcNCfibt",
"https://stablemanagement.com/.image/ar_4:3%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_1200/MTQ1NDU4NTA1OTM4MTE4NDE3/how-to-feed-a-horse-herd-to-prevent-fights-promo-image.jpg",
"https://www.summertech.net/wp-content/uploads/2020/11/pexels-sharon-mccutcheon-1909802-scaled.jpg",
"https://cdn.britannica.com/47/103847-050-8E18B710/varieties-apples.jpg",
"https://i.kym-cdn.com/photos/images/original/001/423/320/be4.jpg",
"https://i.chzbgr.com/full/9236027136/h84021D97/apple-from-fortnite-into-a-real-thing-above-a-pic-of-an-apple-from-fortnite-next-to-a-real-apple",
"https://i.kym-cdn.com/photos/images/newsfeed/001/341/514/c31.jpg",
"https://townsquare.media/site/71/files/2021/02/Newburgh-Walmart.jpg?w=980&q=75"
"https://static.toiimg.com/thumb/msid-83848108,width-800,height-600,resizemode-75,imgsize-611601,pt-32,y_pad-40/83848108.jpg",
"https://i.ytimg.com/vi/kH0SwGJhZLs/maxresdefault.jpg",
"https://freepngimg.com/thumb/mario/20723-2-mario-image.png",
"https://www.citypng.com/public/uploads/preview/-41601314003cc85anibww.png",
"https://cdn.akamai.steamstatic.com/steam/apps/945360/capsule_616x353.jpg?t=1625742109",
"https://manofmany.com/wp-content/uploads/2020/10/Best-Among-Us-Memes-6.jpg",
"https://i.kym-cdn.com/editorials/icons/original/000/002/373/violencecover_(1).jpg",
"https://preview.redd.it/babpcjjtqtp51.jpg?width=960&crop=smart&auto=webp&s=45815757294025f79cfa143a76c889cda07fcfcb",
"https://i.redd.it/3836te4sl4m51.jpg",
"https://img.redbull.com/images/q_auto,f_auto/redbullcom/2020/9/23/tfeehptykrj1h8ysv6oi/amongus",
"https://memezila.com/wp-content/This-was-the-hardest-game-of-my-life-meme-6672.png",
"https://lh3.googleusercontent.com/proxy/yg5Nj04S86euD6JrwMoC3ZxSve0PDnMm2nkZNGJpu_geTzX2JNkuRvxvt17wYkIqdZzRqlxvY3ueGlaSH8QqdIViOAc",
"https://memezila.com/wp-content/The-film-is-based-on-true-story-Meanwhile-the-film-meme-4907.png",
"https://pics.me.me/movie-this-movie-is-based-on-a-true-story-also-67291631.png",
"https://64.media.tumblr.com/tumblr_mej0eunZtM1ql3loeo1_500.png",
"https://memezila.com/wp-content/Its-free-bee-movie-meme-4168.png",
"http://pm1.narvii.com/7059/665623822f0f0b775e52eb6d3c11df95e1a6cbc6r1-615-346v2_uhq.jpg",
"https://ahseeit.com//king-include/uploads/2019/03/51717682_529338877899326_7148573042683013631_n-2148471130.jpg",
"https://youtu.be/dQw4w9WgXcQ",












]


if win == True:
    print("WE HAVE A WINNER therefore you get this ILLEGAL MEME")
    success = random.randint(0,len(links))
    print("you got image number ", success, "!!!" )
    webbrowser.open(links[success])

