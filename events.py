import discord
from discord.ext import commands
from response_anime import response

class ComandosBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()  
    async def on_ready(self):  
        print("O Bot tá online")  
      
    @commands.command()  
    async def soma(self, ctx, n1: int, n2: int):  
        r = n1 + n2  
        await ctx.reply(r)  
      
    @commands.command()
    async def info(self, ctx, *, nome_anime):
        try:
        	info = response(nome_anime)

        	embed = discord.Embed(
        	title=f"{info.get('titulo', 'Título desconhecido')}",
            color=discord.Color.blue()
        )
        	embed.add_field(name="Ano:", value=f"{info.get('ano', 'Desconhecido')}", inline=False)
        	embed.add_field(name="Episódios", value=f"{info.get('episodios', 'Desconhecido')}")
        	embed.add_field(name="Status", value=f"{info.get('status', 'Desconhecido')}")
        	embed.add_field(name="Nota", value=f"{info.get('nota', 'Sem nota')}")
        	embed.add_field(name="Gêneros", value=f"{info.get('generos', 'Desconhecido')}")

        	await ctx.reply(embed=embed)
        except Exception as e:
        	print(f"Erro no comando info: {e}")
        	await ctx.reply("Não consegui pegar as informações desse anime. Tenta outro nome!")


async def setup(bot):
    await bot.add_cog(ComandosBot(bot))
    
if __name__ == "__main__":
	print(response("naruto"))