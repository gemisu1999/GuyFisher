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
a5=""

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
        a = random.randrange(1,5)
        if a==1:
            d=a1
        elif a==2:
            d=a2
        elif a==3:
            d=a3
        elif a==4:
            d=a4
        else:
            d=a5
        await msg.channel.send(d)

    if '사랑해' in msg.content and ('파비오'and'글 읽어'and'바보'and'힘들어'and'힘들다'and'안 할'and'안할') not in msg.content:
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
    
    
    if '파비오' in msg.content and ('사랑해'and'글 읽어'and'바보'and'힘들어'and'힘들다'and'안 할'and'안할') not in msg.content:
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

    if '바보' in msg.content and ('사랑해'and'파비오'and'글 읽어'and'힘들어'and'힘들다'and'안 할'and'안할') not in msg.content:
        a = random.randrange(1,3)
        if a==1:
            d=e1
        elif a==2:
            d=e2
        else:
            d=e3
        await msg.channel.send(d)

    if '힘들어' in msg.content and ('사랑해'and'파비오'and'글 읽어'and'바보'and'힘들다'and'안 할'and'안할') not in msg.content:
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

    if '힘들다' in msg.content and ('사랑해'and'파비오'and'글 읽어'and'힘들어'and'바보'and'안 할'and'안할') not in msg.content:
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

    if '안 할' in msg.content and ('사랑해'and'파비오'and'글 읽어'and'힘들어'and'힘들다'and'바보'and'안할') not in msg.content:
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
        
    if '안할' in msg.content and and ('사랑해'and'파비오'and'글 읽어'and'힘들어'and'힘들다'and'안 할'and'바보') not in msg.content:
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



# 봇 실행
access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
