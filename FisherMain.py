import discord
from discord.ext import commands
import random
import emoji
import os

intents = discord.Intents.all()
intents.messages = True
bot = commands.Bot(command_prefix='!', help_command=None, case_insensitive=True, intents=intents)

#글 읽어줘
a1="바다는 비에 젖지 않는다\r\n- 어니스트 헤밍웨이, 노인과 바다"
a2="인간은 패배하도록 만들어진 것은 아니다.\r\n인간은 파괴될 지언정 패배할 수는 없다.\r\n- 어니스트 헤밍웨이, 노인과 바다"
a3="내 속에서 솟아나오려는 것,\r\n바로 그것을 나는 살아보려고 했다.\r\n왜 그것이 그토록 어려웠을까?\r\n- 헤르만 헤세,데미안"
a4="어느 추운 겨울 날,\r\n나는 드디어 내 안에 아무도 꺾을 수 없는 여름이 있다는 것을 알게 되었다.\r\n- 알베르 카뮈"
a5="그 때는 다른 사람 이었기 때문에 어제로 돌아갈 수 없습니다.\r\n- 잃어버린 낙원, 존 밀턴"
a6="나는 홀몸으로 세상에 나왔으니,\r\n홀몸으로 돌아가야 한다.\r\n- 미겔 데 세르반테스, 돈키호테"
a7="당신은 결국 그대로의 당신일 뿐이오.\r\n아무리 곱슬머리 가발을 쓰고 굽 높은 신발을 신어도\r\n당신은 언제까지나 당신일 뿐이오.\r\n- 요한 폰 괴테, 파우스트"
a8="그 사람이 나를 때리고, 나는 그 사람을 사랑하고,\r\n그 사람을 사랑하는지는 잘 모르겠으나 나는 맞고만 있고, 그런 일이 매일 반복되므로\r\n내가 그 사람을 사랑하는 게 틀림없다.\r\n- 훌리오 코르타사르, 드러누운 밤"
a9="누구나 별을 하나 갖고 있다는 거요. 자신의 정직함이라는 별을요.\r\n우린 그걸 찾기 위해 인생을 다 써버려요.\r\n- 아서 밀러, 모두가 나의 아들"
a10=""

#사랑해
b1="…고마워요, 정말로."
b2="내가… 그에게 정말 듣고싶은 말이네요."
b3="*(그저 웃음을 지을 뿐 답을 하지는 않았다.)*"
b4=""

#파비오
c1="…그를 알아요?"
c2="파비오는… 내겐 잊을 수 없는 친구예요. 동시에 놓지 못할 적이기도 하죠."
c3="사랑한다고… 언젠가는 진심을 다해 전하고 싶어요."
c4="파비오 이 바보…. *(중얼거리는 목소리가 한참 이어졌다.)*"
c5="미워… 내가 노력하는 거 알면서…. *(울먹이는 목소리가 중얼거린다.)*"
c6=""

#바보
e1="끄응…. 화났어요? 내가 미안해요."
e2="바, 바보?! 내, 내가 뭘 했다고…."
e3=""

#힘들어
f1="…피곤하면 잠시 쉬어가는 건 어때요? 나도 이런 말 할 자격은 없지만 쉬는 것도 도움은 되거든요."
f2="조금만 참아요, 같이 힘내보죠. 내가 옆에서 도와줄게요."
f3="많이 힘들어요? 괜찮으면 좋겠는데…."
f4="걱정마요, 그건 잘 하고있다는 증거니까."
f5=""

#안 할래
g1="그렇게 안 하려고만 하면 안 돼요…. 어서 펜 들어요."
g2="움직여요! 시간은 지금도 흘러가고 있다구요."
g3="…안 하는 버릇 계속 들이면 진짜 다 포기하는데. 게으르게 사는 건 딱히 좋지 않은 방법이라고 충고하죠."
g4="단정지어서 포기하면 나도 할 말이 없는데. 정말 그럴 거예요? *(단호한 목소리다.)*"
g5=""

#밥 먹었어?
h1="음… 출출하긴 하네요. 파비오가 오면 같이 먹어야겠어요."
h2="아까 사라 밥 먹이면서 남은 거 먹었어요. 당신은요?"
h3="…입맛이 없어요. 나중에 챙길래요."
h4="(피곤한 얼굴로 고개만을 저었다.)"
h5="외식하기로 해서 기다리고 있어요. 나이가 드니까 밥을 챙겨먹는 게 어렵네요."
h6=""

@bot.event
async def on_ready():             # 봇 실행 시 실행되는 함수
    print(f'{bot.user} 에 로그인하였습니다!')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('운동'))

@bot.event
async def on_message(msg):
    if msg.author.bot: return None
    await bot.process_commands(msg)

@bot.command()
async def about(ctx):    
    embed = discord.Embed(title='명령어', 
                            description='"책 읽어줘" : 랜덤으로 책의 한 구절을 읽어준다.\r\n"좋은 아침" : 파비오가 아침인사를 해준다.\r\n"좋은 밤" : 파비오가 저녁인사를 해준다.')
    await ctx.channel.send(embed=embed)

@bot.event
async def on_message(msg):    
    if '글 읽어' in msg.content:
        a = random.randrange(1,10)
        if a==1:
            d=a1
        elif a==2:
            d=a2
        elif a==3:
            d=a3
        elif a==4:
            d=a4
        elif a==5:
            d=a5
        elif a==6:
            d=a6
        elif a==7:
            d=a7
        elif a==8:
            d=a8
        elif a==9:
            d=a9
        else:
            d=a10
        await msg.channel.send(d)

    if '사랑해' in msg.content:
        a = random.randrange(1,4)
        if a==1:
            d=b1
        elif a==2:
            d=b2
        elif a==3:
            d=b3
        else:
            d=b4
        await msg.channel.send(d)
    
    
    if '파비오' in msg.content:
        a = random.randrange(1,6)
        if a==1:
            d=c1
        elif a==2:
            d=c2
        elif a==3:
            d=c3
        elif a==4:
            d=c4
        elif a==5:
            d=c5
        else:
            d=c6
        await msg.channel.send(d)

    if '바보' in msg.content:
        a = random.randrange(1,3)
        if a==1:
            d=e1
        elif a==2:
            d=e2
        else:
            d=e3
        await msg.channel.send(d)

    if '힘들어' in msg.content:
        a = random.randrange(1,5)
        if a==1:
            d=f1
        elif a==2:
            d=f2
        elif a==3:
            d=f3
        elif a==4:
            d=f4
        else:
            d=f5
        await msg.channel.send(d)

    if '힘들다' in msg.content:
        a = random.randrange(1,5)
        if a==1:
            d=f1
        elif a==2:
            d=f2
        elif a==3:
            d=f3
        elif a==4:
            d=f4
        else:
            d=f5
        await msg.channel.send(d)

    if '안 할' in msg.content:
        a = random.randrange(1,5)
        if a==1:
            d=g1
        elif a==2:
            d=g2
        elif a==3:
            d=g3
        elif a==4:
            d=g4
        else:
            d=g5
        await msg.channel.send(d)
        
    if '안할' in msg.content:
        a = random.randrange(1,5)
        if a==1:
            d=g1
        elif a==2:
            d=g2
        elif a==3:
            d=g3
        elif a==4:
            d=g4
        else:
            d=g5
        await msg.channel.send(d)
        
    if '밥 먹었' in msg.content:
        a = random.randrange(1,6)
        if a==1:
            d=h1
        elif a==2:
            d=h2
        elif a==3:
            d=h3
        elif a==4:
            d=h4
        elif a==5:
            d=h5
        else:
            d=h6
        await msg.channel.send(d)



# 봇 실행
access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
