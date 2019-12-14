
import getinfo as gi
import process as p
import insert
def main():
    url=insert.insert()
    html=gi.Getinfo(url)
    p.Process(html)

main()
