import argparse


PSSTGUY_TEMPLATE = """
┻┳| 
┻┳| 
┳┻| 
┳┻| 
┻┳| 
┳┻| 
┻┳| 
┳┻| _
┻┳|•.•)   {SECRET_TXT}
┳┻|⊂ﾉ    
┻┳|
"""


def psstguy(secret_txt):
    return PSSTGUY_TEMPLATE.format(SECRET_TXT=secret_txt)


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('secret', type=str, help='Text to whisper')
    args = parser.parse_args()
    print(psstguy(args.secret))


if __name__ == '__main__':
    cli()
