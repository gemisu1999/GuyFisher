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
b4="그 사랑을 받을 만큼 전 좋은 사람이 아닌걸요... 그래도, 고마워요."
b5="그, ... 한 번만 더 말해주세요."
b6="... 그건 내 최고의 방어이자 그의 무기죠."
b7="...나도 그렇다고, 그에게 말하고 싶어요."
b8="나도요. 고마워요, 정말."
b9=""

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

#주물주물
i1="으,학! 뭐 하는 거예요! (많이 당황한 눈치로 바라본다.)"
i2="*(사색이 된 채 허공을 응시하고 있다.)*"
i3="끄으응...하, 하지마요. 정말로..."
i4="마,마,마,만지지 마요! *(격렬하게 반항한다.)*"
i5="이러면 안, 안 돼요... *(얼굴이 새빨갛다.)*"
i6="(작은 목소리로) ...파, 파비오 한테 이를 거예요! 비겁하다고 해도 소용 없어요!"
i7=""

#사라
j1="그 아이에겐… 언제나 죄책감을 가지고 있어요. 내가 더 잘 했다면 보호해줄 수 있었을 텐데."
j2="사라. 사라 자칼로네. 파비오가 사랑하는 아이예요. 그의 가족이죠."
j3="사라는... 착해요. 밥도 잘 먹고 씩씩하죠. 요즘은 잠투정을 조금 부리지만요, 하하."
j4="어른이 될 때까지 아이를 볼 수 있어서 기뻐요, 정말로. 하지만... 미래가 걱정되기도 하네요. 지금처럼 아이 눈을 제대로 맞추고 지낼 수 있을지..."
j5="난 진심으로 사라를 사랑으로 키우고 있어요. 아이가 행복하길 바라죠."
j6="... 우리 애 똑똑하다니까요? 알파벳을 적는데 어찌나 깔끔하게 쓰던지. 자라서 어떤 일을 할지 너무 기대가 되지 않아요? 하하!"
j7="사랑한다, 사라. 아가. 삼촌은 널 정말로 사랑해."
j8="...미안해, 정말 미안해. 그래도 너를 사랑한단다, 사라."
j9=""

#불사의 술
k1="...그건 존재해선 안 됐어요."
k2="그때를 떠올리면 아직도 파비오를 용서할 수 없어요. 내가 이렇게 되는 걸 원한 게 아닌데..."
k3="...요새 내가 사람이 아닌 것 같아요. 그냥..., 언제까지 이렇게 살 수 있을까요."
k4="어째서 영생을 원하는 걸까요? 세상을 살기엔 충분한데."
k5="... 파비오가 자기 자신을 해치는 걸 봤어요. 난... 그게 너무 무서워요. 파비오가 달라질까봐. 사람을 벗어날까봐."
k6="...그날로 돌아가면 절대로 마시지 않을 거예요."
k7="가끔 상상하곤 해요. 욕조에서 피를 하루종일 흘려도 안 죽을까... 하하, 너무 어두운 얘기죠. 미안합니다."
k8=""

#좋은 아침
l1="좋은 아침, 오늘도 힘내요."
l2="날이 좋네요.  낮에는 사라를 데리고 나가봐야겠어요."
l3="Good morning, my friend."
l4="아아, 파비오 한테 인사한다고 해놓고 또 자버렸어요! *(굉장히 슬픈 목소리다.)*"
l5="*(약에 취했는지 고개를 푹 숙인 채 손만 들어 흔든다.)*"
l6="오늘이 어떤 날이 되더라도 항상 즐거웠으면 좋겠어요."
l7="아침 인사를 받을 때마다 얼마나 기쁜지 모를 거예요, 당신은. 고마워요."
l8=""

@bot.event
async def on_ready():             # 봇 실행 시 실행되는 함수
    print(f'{bot.user} 에 로그인하였습니다!')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('사라와 독서'))

@bot.command()
async def about(ctx):    
    embed = discord.Embed(title='명령어', 
                            description='"책 읽어줘" : 랜덤으로 책의 한 구절을 읽어준다.\r\n"좋은 아침" : 파비오가 아침인사를 해준다.\r\n"좋은 밤" : 파비오가 저녁인사를 해준다.')
    await ctx.channel.send(embed=embed)

@bot.event
async def on_message(msg): 
    if msg.author.bot:
        return
    
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
        a = random.randrange(1,9)
        if a==1:
            d=b1
        elif a==2:
            d=b2
        elif a==3:
            d=b3
        elif a==4:
            d=b4
        elif a==5:
            d=b5
        elif a==6:
            d=b6
        elif a==7:
            d=b7
        elif a==8:
            d=b8
        else:
            d=b9
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

    if '주물주물' in msg.content:
        a = random.randrange(1,7)
        if a==1:
            d=i1
        elif a==2:
            d=i2
        elif a==3:
            d=i3
        elif a==4:
            d=i4
        elif a==5:
            d=i5
        elif a==6:
            d=i6
        else:
            d=i7
        await msg.channel.send(d)

    if '사라' in msg.content:
        a = random.randrange(1,9)
        if a==1:
            d=j1
        elif a==2:
            d=j2
        elif a==3:
            d=j3
        elif a==4:
            d=j4
        elif a==5:
            d=j5
        elif a==6:
            d=j6
        elif a==7:
            d=j7
        elif a==8:
            d=j8
        else:
            d=j9
        await msg.channel.send(d)
        
    if '불사의 술' in msg.content:
        a = random.randrange(1,8)
        if a==1:
            d=k1
        elif a==2:
            d=k2
        elif a==3:
            d=k3
        elif a==4:
            d=k4
        elif a==5:
            d=k5
        elif a==6:
            d=k6
        elif a==7:
            d=k7
        else:
            d=k8
        await msg.channel.send(d)

    if '좋은 아침' in msg.content:
        a = random.randrange(1,8)
        if a==1:
            d=l1
        elif a==2:
            d=l2
        elif a==3:
            d=l3
        elif a==4:
            d=l4
        elif a==5:
            d=l5
        elif a==6:
            d=l6
        elif a==7:
            d=l7
        else:
            d=l8
        await msg.channel.send(d)



# 봇 실행
access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
