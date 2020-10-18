import calendar
import datetime
import time
import colorama
from colorama import init
from colorama import Fore, Back, Style
from datetime import date

init()

#Creating the Calendar class and formatting it as a rext calendar
cal = calendar.TextCalendar(firstweekday=6)
currentYear = cal.formatyear(2020, w=2, l=1, c=6, m=3)

#Getting this year through datetime
thisYear = date.today().year

#Getting the current day's date through datetime
todaysDate = date.today()

todaysDay = str(todaysDate)[8:10]
todaysMonth = str(todaysDate)[6:7]

#Defining colors for colorama
redText = Fore.RED
brightText = Style.BRIGHT
whiteText = Fore.WHITE
cyanText = Fore.CYAN
greenText = Fore.GREEN

#Villager birthday dictionaries
januaryPairs = {}
februaryPairs = {}
marchPairs = {}
aprilPairs = {}
mayPairs = {}
junePairs = {}
julyPairs = {}
augustPairs = {}
septemberPairs = {}
octoberPairs = {}
novemberPairs = {}
decemberPairs = {}

#Villager Birthdays
allBirthdays = [januaryPairs, februaryPairs, marchPairs, aprilPairs, mayPairs, junePairs, julyPairs, augustPairs, septemberPairs, octoberPairs, novemberPairs, decemberPairs]

#Function to go through month lists and generate a key value pair for each villager, then add it to the respective month's dictionary
def villager_birthday(monthList, monthPairs, monthNum):
    for x in monthList:
        name = x[7:20]
        day = x[0:2]

        newDate = str(thisYear) + ", " + str(monthNum) + ", " + str(day)

        monthPairs.update({name:newDate})

januaryList = [
'01st - Bob',
'02nd - Poncho',
'03rd - Joey',
'04th - Diana',
'05th - Roald',
'06th - Carmen',
'06th - Felyne',
'07th - Harry',
'08th - Pierce',
'09th - Tiffany',
'10th - Papi',
'11th - Maddie',
'12th - Moe',
'13th - Puddles',
'14th - Velma',
'15th - Gladys',
'16th - Ursala',
'17th - Rizzo',
'19th - Simon',
'20th - Opal',
'21st - Genji',
'22nd - Francine',
'23rd - Gwen',
'24th - Rhonda',
'25th - Savannah',
'26th - Vivian',
'27th - Aurora',
'27th - Admiral',
'28th - Margie',
'29th - Cube',
'30th - Flurry',
'31st - Winnie'
]

villager_birthday(januaryList, januaryPairs, 1)

februaryList = [
'01st - Bill',
'02nd - Jitters',
'03rd - Olivia',
'04th - Lily',
'05th - Penelope',
'06th - Annalisa',
'07th - Boomer',
'08th - Frobert',
'09th - Flora',
'09th - Cleo',
'10th - Stitches',
'11th - Pompom',
'12th - Drago',
'13th - Ribbot',
'14th - Muffy',
'15th - Kitty',
'16th - Anabelle',
'17th - Dobie',
'18th - Dora',
'19th - Freckles',
'20th - Sprinkle',
'21st - Puck',
'21st - Ganon',
'22nd - Avery',
'23rd - Pate',
'24th - Anicotti',
'25th - Hamphrey',
'26th - Sheldon',
'27th - Rosie',
'28th - Naomi'
]

villager_birthday(februaryList, februaryPairs, 2)

marchList = [
'01st - Coco',
'02nd - Barold',
'03rd - Bonbon',
'04th - Anchovy',
'05th - Gala',
'06th - Chevre',
'06th - Chai',
'07th - Molly',
'08th - Zucker',
'09th - Cyrano',
'11th - Hopkins',
'12th - Midge',
'14th - Dotty',
'15th - Julian',
'16th - Doc',
'17th - Cheri',
'19th - Merengue',
'20th - Hornsby',
'21st - Elise',
'22nd - Paula',
'23rd - Axel',
'24th - Skye',
'25th - Celia',
'25th - Billy',
'26th - Fauna',
'26th - Louie',
'27th - Lolly',
'28th - Baabara',
'29th - Biff',
'30th - Felicity',
'31st - Klaus'
]

villager_birthday(marchList, marchPairs, 3)

aprilList = [
'01st - Tammi',
'02nd - Cashmere',
'03rd - Eunice',
'04th - Buck',
'05th - Beau',
'06th - Hopper',
'07th - Rasher',
'08th - Maelle',
'09th - Stella',
'10th - Shari',
'11th - Punchy',
'12th - Melba',
'13th - Candi',
'14th - Rocket',
'16th - Vesta',
'16th - Marty',
'17th - Charlise',
'18th - Piper',
'19th - Pietro',
'20th - Stu',
'21st - Agnes',
'22nd - Phoebe',
'23rd - Miranda',
'24th - Walt',
'25th - Bertha',
'26th - Kevin',
'27th - Katt',
'28th - Ava',
'29th - Coach',
'30th - Angus'
]

villager_birthday(aprilList, aprilPairs, 4)

mayList = [
'01st - Clyde',
'02nd - Mint',
'03rd - Sylvia',
'04th - Deirdre',
'05th - Paolo',
'06th - Tank',
'07th - Ozzie',
'08th - Curlos',
'09th - Bunnie',
'10th - Patty',
'11th - Cherry',
'12th - Ellie',
'13th - Biskit',
'14th - Canberra',
'15th - Leonardo',
'16th - Ike',
'17th - Gayle',
'18th - Pekoe',
'19th - Olaf',
'20th - T-Bone',
'21st - June',
'22nd - Colton',
'23rd - Peggy',
'24th - Deli',
'25th - Derwin',
'26th - Bruce',
'27th - Del',
'28th - Renée',
'28th - Cece',
'29th - Purrl',
'30th - Hamlet',
'31st - Marcie'
]

villager_birthday(mayList, mayPairs, 5)

juneList = [
'01st - Keaton',
'02nd - Lucy',
'02nd - Inkwell',
'03rd - Filbert',
'05th - Camofrog',
'06th - Raddle',
'07th - Zell',
'08th - Peanut',
'09th - Alfonso',
'10th - Walker',
'11th - Pudge',
'12th - Bettina',
'13th - Scoot',
'14th - Pippy',
'15th - Maple',
'16th - Roscoe',
'17th - Tangy',
'17th - Spike',
'18th - Cookie',
'19th - Sally',
'20th - Graham',
'21st - Sydney',
'22nd - Jacques',
'23rd - Tammy',
'24th - Bluebear',
'25th - Drake',
'26th - Marina',
'27th - Deena',
'28th - Kidd',
'29th - Merry',
'30th - Broccolo',
'30th - Weber'
]

villager_birthday(juneList, junePairs, 6)

julyList = [
'01st - Curt',
'02nd - Agent S',
'03rd - Blaire',
'04th - Apollo',
'05th - Samson',
'06th - Mira',
'07th- Bree',
'07th- Viché',
'08th - Jeremiah',
'09th - Static',
'09th - Huck',
'10th - Mott',
'10th - Toby',
'11th - Victoria',
'11th - Filly',
'12th - Olive',
'13th - Twiggy',
'14th - Dizzy',
'15th - Caroline',
'16th - Frita',
'17th - Jay',
'18th - Croque',
'19th - Nibbles',
'20th - Yuka',
'21st - Prince',
'22nd - Chow',
'23rd - Elvis',
'24th - O\'Hare',
'24th - Rex',
'25th - Peck',
'26th - Curly',
'27th - Erik',
'27th - Ketchup',
'28th - Truffles',
'29th - Lionel',
'30th - Frank',
'31st - Grizzly',
'31st - Julia'
]

villager_birthday(julyList, julyPairs, 7)

augustList = [
'01st - Kid Cat',
'02nd - Vladimir',
'03rd - Benjamin',
'03rd - Tad',
'04th - Bones',
'05th - Poppy',
'06th - Chester',
'07th - Rory',
'07th - Boots',
'08th - Bud',
'09th - Soleil',
'10th - Cole',
'11th - Gigi',
'12th - Gloria',
'13th - Tabby',
'14th - Rod',
'14th - Leopold',
'15th - Wendy',
'16th - Nate',
'17th - Stinky',
'18th - Rocco',
'19th - Alice',
'19th - Tybalt',
'20th - Lopez',
'21st - Wart Jr.',
'22nd - Rolf',
'23rd - Nana',
'24th - Nan',
'24th - Jacob',
'25th - Tipper',
'26th - Rowan',
'27th - Bangle',
'28th - Chrissy',
'29th - Gruff',
'30th - Hazel'
]

villager_birthday(augustList, augustPairs, 8)

septemberList = [
'01st - Violet',
'02nd - Flo',
'03rd - Spork',
'03rd - Maggie',
'04th - Cally',
'05th - Greta',
'06th - Cesar',
'07th - Tucker',
'08th - Astrid',
'09th - Pinky',
'10th - Pecan',
'11th - Peewee',
'12th - Boone',
'13th - Moose',
'14th - Ricky',
'15th - Tutu',
'16th - Ed',
'17th - Whitney',
'18th - Bubbles',
'19th - Fuchsia',
'20th - Octavian',
'20th - Norma',
'21st - Henry',
'22nd - Ankha',
'23rd - Cranston',
'24th - Apple',
'25th - Mitzi',
'26th - Teddy',
'27th - Beardo',
'28th - Kody',
'29th - Marshal',
'30th - Monique'
]

villager_birthday(septemberList, septemberPairs, 9)

octoberList = [
'01st - Boyd',
'02nd - Diva',
'03rd - Big Top',
'04th - Goose',
'05th - Elmer',
'06th - Tex',
'06th - Bitty',
'07th - Cobb',
'08th - Kiki',
'09th - Drift',
'10th - Benedict',
'11th - Kitt',
'12th - Lyman',
'12th - Plucky',
'13th - Chops',
'13th - Gonzo',
'14th - Egbert',
'15th - Hippeux',
'15th - Bea',
'16th - Friga',
'17th - Limberg',
'18th - Al',
'19th - Clay',
'20th - Antonio',
'21st - Timbra',
'21st - Sandy',
'22nd - Sylvana',
'23rd - Groucho',
'24th - Broffina',
'24th - Snooty',
'25th - Portia',
'26th - Eugene',
'27th - Jambette',
'28th - Gaston',
'29th - Rodeo',
'30th - Wade'
]

villager_birthday(octoberList, octoberPairs, 10)

novemberList = [
'01st - Butch',
'01st - Rilla',
'02nd - Iggly',
'03rd - Snake',
'04th - Lucky',
'05th - Lobo',
'06th - Boris',
'07th - Bam',
'08th - Alli',
'09th - Pango',
'10th - Rodney',
'11th - Mac',
'12th - Mathilda',
'13th - Queenie',
'14th - Pancetti',
'15th - Sly',
'16th - Daisy',
'17th - Mallary',
'18th - Tia',
'19th - Amelia',
'20th - Sparro',
'21st - Flip',
'21st - Epona',
'22nd - Claudia',
'23rd - Knox',
'24th - Shep',
'25th - Wolfgang',
'26th - Willow',
'27th - Phil',
'28th - Peaches',
'29th - Kabuki',
'30th - Tasha'
]

villager_birthday(novemberList, novemberPairs, 11)

decemberList = [
'01st - Rooney',
'01st - Sprocket',
'02nd - Annalise',
'02nd - Wolf Link',
'03rd - Claude',
'04th - Robin',
'05th - Hans',
'05th - Carrie',
'06th - Kyle',
'07th - Monty',
'07th - Buzz',
'08th - Eloise',
'09th - Becky',
'10th - Tom',
'11th - Sterling',
'12th - Lucha',
'13th - Bianca',
'13th - Medli',
'14th - Freya',
'15th - Chadder',
'16th - Gabi',
'17th - Cousteau',
'18th - Fang',
'19th - Chief',
'20th - Rudy',
'21st - Blanche',
'22nd - Quillson',
'23rd - Ken',
'25th - Ruby',
'26th - Pashmina',
'27th - Goldie',
'28th - Bella',
'29th - Vic',
'29th - Murphy',
'30th - Hugh',
'31st - Marcel'
]

villager_birthday(decemberList, decemberPairs, 12)

#Holidays using calendar module
#cherryblossom = #April 1 - 10

#Switch-case function for weekdays
def weekday_switch(dayNum):
    switcher = {
    1 : calendar.MONDAY,
    2 : calendar.TUESDAY,
    3 : calendar.WEDNESDAY,
    4 : calendar.THURSDAY,
    5 : calendar.FRIDAY,
    6 : calendar.SATURDAY,
    7 : calendar.SUNDAY
    }
    return switcher.get(dayNum)

#Function to find specific days of the month
def find_day(range1, range2, weekNum, day):
    for month in range (range1,range2):
        mycal = calendar.monthcalendar(thisYear, month)
        week1 = mycal[weekNum - 1]
        week2 = mycal[weekNum]
        if week1[weekday_switch(day)] != 0:
            if week1[weekday_switch(day)] <= (weekNum - 1) * 7:
                theDay = week2[weekday_switch(day)]
            else:
                theDay = week1[weekday_switch(day)]
        else:
            theDay = week2[weekday_switch(day)]

        return [thisYear, month, theDay]

def event(eventName, eventDate, eventPairs):
    eventPairs.update({eventName:eventDate})

januaryEvents = {}
februaryEvents = {}
marchEvents = {}
aprilEvents = {}
mayEvents = {}
juneEvents = {}
julyEvents = {}
augustEvents = {}
septemberEvents = {}
octoberEvents = {}
novemberEvents = {}
decemberEvents = {}

allEvents = [januaryEvents, februaryEvents, marchEvents, aprilEvents, mayEvents, juneEvents, julyEvents, augustEvents, septemberEvents, octoberEvents, novemberEvents, decemberEvents]

event("New Year's Day", [2020, 1, 1], januaryEvents)
event("Groundhog's Day", [2020, 2, 2], februaryEvents)
event("Valentine's Day", [2020, 2, 14], februaryEvents)
event("Festivale", [2020, 2, 24], februaryEvents)
event("Shamrock Day", [2020, 3, 17], marchEvents)
event("Bunny Day", [2020, 4, 12], aprilEvents)
event("April Fool's Day", [2020, 4, 1], aprilEvents)
event("Nature Day", [2020, 4, 22], aprilEvents)
event("Summer Solstice", [2020, 6, 21], juneEvents)
event("Halloween", [2020, 10, 31], octoberEvents)
event("Winter Solstice", [2020, 12, 21], decemberEvents)
event("Toy Day", [2020, 12, 24], decemberEvents)
event("New Year's Eve", [2020, 12, 31], decemberEvents)

#Find which days are fishing tourney days

#Third Saturday
event("Fishing Tourney 1", find_day(1, 2, 3, 6), januaryEvents)
event("Fishing Tourney 3", find_day(3, 4, 3, 6), marchEvents)
event("Fishing Tourney 5", find_day(5, 6, 3, 6), mayEvents)
event("Fishing Tourney 7", find_day(11, 12, 3, 6), novemberEvents)

#Second Saturday
event("Fishing Tourney 2", find_day(2, 3, 2, 6), februaryEvents)
event("Fishing Tourney 4", find_day(4, 5, 2, 6), aprilEvents)
event("Fishing Tourney 6", find_day(10, 11, 2, 6), octoberEvents)
event("Fishing Tourney 8", find_day(12, 13, 2, 6), decemberEvents)


#Find which days are bugoff days
event("Bug-off 1", find_day(6, 7, 3, 6), juneEvents)
event("Bug-off 2", find_day(7, 8, 3, 6), julyEvents)
event("Bug-off 3", find_day(8, 9, 3, 6), augustEvents)
event("Bug-off 4", find_day(9, 10, 3, 6), septemberEvents)

#find which day is mother's day
event("Mother's Day", find_day(5, 6, 2, 7), mayEvents)

#Find which day is Father's Day
event("Father's Day", find_day(6, 7, 3, 7), juneEvents)

#find which days have fireworks
def all_august():
    first = find_day(8, 9, 1, 7)
    second = find_day(8, 9, 2, 7)
    third = find_day(8, 9, 3, 7)
    fourth = find_day(8, 9, 4, 7)

    if int(fourth[2]) < 25:
        fifth = find_day(8, 9, 5, 7)

all_august()

#Find which day is Labor day
event("Labor Day", find_day(9, 10, 1, 1), septemberEvents)

#Find which day is explorer day
event("Explorer Day", find_day(10, 11, 2, 1), octoberEvents)

#Find which day is Harvest Day
event("Harvest Day", find_day(11, 12, 4, 4), novemberEvents)

print(brightText + greenText + "\n\nGreetings! This tool will show you upcoming dates in Animal Crossing: New Leaf this month!")

time.sleep(3)

for key, value in allEvents[int(todaysMonth) - 1].items():
    name = str(key)
    date = str(value)

    if int(date[10:12]) > int(todaysDay):
        print(whiteText + "\n\nHere are the " + redText + "event(s) " + whiteText + "that are coming up: \n")

        print(redText + name + whiteText + " is in " + str(int(date[10:12]) - int(todaysDay)) + " day(s)! " + cyanText + "(" + date[7:8] + "/" + date[10:12] + ")")
        time.sleep(.75)
    elif int(date[10:12]) == int(todaysDay):
        print(whiteText + "\n\nHere are the " + redText + "event(s) " + whiteText + "that are coming up: \n")

        print(redText + name + whiteText + " is " + cyanText + "today!")
        time.sleep(.75)
    elif int(date[10:12]) < int(todaysDay):
        print(whiteText + "\n\nThere are no " + redText + "event(s) " + whiteText + "left this month. \n")

time.sleep(3)

print(whiteText + "\n\nHere are the " + redText + "birthday(s) " + whiteText + "that are coming up this month: \n")
for key, value in allBirthdays[int(todaysMonth) - 1].items():
    name = str(key)
    birthdate = str(value)

    if int(birthdate[9:11]) > int(todaysDay):
        print(redText + name + whiteText + "'s birthday is in " + str(int(birthdate[9:11]) - int(todaysDay)) + " day(s)! " + cyanText + "(" + birthdate[6:7] + "/" + birthdate[9:11] + ")")
        time.sleep(.5)
    elif int(birthdate[9:11]) == int(todaysDay):
        print(redText + name + whiteText + "'s birthday is " + cyanText + "today!")
        time.sleep(.5)

input("\n\nPress enter to exit. . .")

print("\n\n")
