import requests
from bs4 import BeautifulSoup
import html5lib  # Ensure this is imported

# horoscopes = ['aries','taurus','gemini','cancer','leo','virgo','libra','scorpio','sagittarius','capricorn','aquarius','pisces']
# while True:
#   flag = False
#   horoscope = input("enter your horoscope ").lower()
#   for hr in horoscopes :
#     if hr == horoscope :
#       print("displaying horoscope for " , hr)
#       flag = True
#       break
#   if flag == True:
#     break
#   print("please check the spelling of your input")

def time_today(horoscope_Data):
    today_horoscope = get_horoscope("https://astrotalk.com/horoscope/todays-horoscope/{}".format(horoscope_Data.lower()))
    # structuring todays horoscope data
    your_horoscope = {}
    for thr in today_horoscope :
        try :
            thr = thr.split(":")
            your_horoscope[thr[0]]  = thr[1]
        except :
            continue
    return your_horoscope

def time_tomorrow(horoscope_Data):
    tomorrow_horoscope = get_horoscope("https://astrotalk.com/horoscope/tomorrow-horoscope/{}".format(horoscope_Data.lower()))
    # structuring tomorrows horoscope data
    your_horoscope = {}
    for thr in tomorrow_horoscope :
        try :
            thr = thr.split(":")
            your_horoscope[thr[0]]  = thr[1]
        except :
            continue
    return your_horoscope

def time_week(horoscope_Data):
    weekly_horoscope = get_horoscope("https://astrotalk.com/horoscope/weekly-horoscope/{}".format(horoscope_Data.lower()))
    # structuring tomorrows horoscope data
    your_horoscope = {}
    for thr in weekly_horoscope :
        try :
            thr = thr.split(":")
            your_horoscope[thr[0]]  = thr[1]
        except :
            continue
    return your_horoscope

def time_yesterday(horoscope_Data):
    yesterdat_horoscope = get_horoscope("https://astrotalk.com/horoscope/yesterday-horoscope/{}".format(horoscope_Data.lower()))
    # structuring tomorrows horoscope data
    your_horoscope = {}
    for thr in yesterdat_horoscope :
        try :
            thr = thr.split(":")
            your_horoscope[thr[0]]  = thr[1]
        except :
            continue
    return your_horoscope


def time_year(horoscope_Data):
    yearly_horoscope = get_horoscope("https://astrotalk.com/horoscope/yearly-horoscope/{}".format(horoscope_Data.lower()))
    # structuring tomorrows horoscope data
    your_horoscope = {}
    yearly_horoscope = [i.strip() for i in yearly_horoscope if i.strip() != ""]
    horoscope_sections = ["Love Horoscope 2024", "Finance Horoscope 2024" , "Career Horoscope 2024" , "Family Horoscope 2024" , "Health Horoscope 2024" , "Marriage Horoscope 2024"]
    yearly_horoscope_sections = []
    yearly_horoscope_sections.append( "Astrological Remedies For {} in 2024:".format(horoscope_Data.title()))
    yearly_horoscope_sections.append( "Astrological Remedies For {} in 2024".format(horoscope_Data.title()))
    for i in horoscope_sections:
        yearly_horoscope_sections.append("{} {}".format(horoscope_Data.title() , i))


    your_horoscope["horoscope"] = []
    i = 0
    while i < len(yearly_horoscope) :
        try :
            if yearly_horoscope[i] in yearly_horoscope_sections:
                # print("section found ... ")
                key = yearly_horoscope[i]
                your_horoscope[key] = []
                i = i+1
                # print(key , i )
                while yearly_horoscope[i] not in yearly_horoscope_sections:
                    your_horoscope[key].append(yearly_horoscope[i])
                    i = i+1
                    # print("adding to key", i , your_horoscope["year"][key] )

            else :
                your_horoscope["horoscope"].append(yearly_horoscope[i])
                i = i+1
                # print("horoscope", i , your_horoscope["year"]["horoscope"] )

        except :
            continue

    return your_horoscope




def time_month(horoscope_Data):
    monthly_horoscope = get_horoscope("https://astrotalk.com/horoscope/monthly-horoscope/{}".format(horoscope_Data.lower()))
    # structuring tomorrows horoscope data
    your_horoscope = {}

    monthly_horoscope = [i.strip() for i in monthly_horoscope if i.strip() != ""]
    monthly_horoscope_sections = ["Love & Relationship" , "Health & Wellness" , "Money & Finances" , "Career" , "Tip of the month:" , "Love and Relationship" , "Health and Wellness" , "Money and Finances" , "Tip of the month"]
    your_horoscope["horoscope"] = []
    i = 0
    while i < len(monthly_horoscope) :
        try :
            if monthly_horoscope[i] in monthly_horoscope_sections:
                # print("section found ... ")
                key = monthly_horoscope[i]
                your_horoscope[key] = []
                i = i+1
                # print(key , i )
                while monthly_horoscope[i] not in monthly_horoscope_sections:
                    your_horoscope[key].append(monthly_horoscope[i])
                    i = i+1
                    # print("adding to key", i , your_horoscope[key] )

            else:
                your_horoscope["horoscope"].append(monthly_horoscope[i])
                i = i+1
                # print("horoscope", i , your_horoscope["horoscope"] )

        except :
            continue
    return your_horoscope


def get_data(horoscope_Data , time): 
    if time == "today" :
        return time_today(horoscope_Data)
    if time == "tomorrow" :
        return time_tomorrow(horoscope_Data)  
    if time == "week" :
        return time_week(horoscope_Data)
    if time == "month" :
        return time_month(horoscope_Data)
    if time == "year" :
        return time_year(horoscope_Data)
    if time == "yesterday" :
        return time_yesterday(horoscope_Data)

def get_horoscope(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    hrblob = soup.find('div', attrs = {'class':'parah_aries_horocope'})
    hrblob.prettify()
    predictions = []
    for row in hrblob :
        predictions.append(row.get_text())

    return predictions




# print("\n============ ",horoscope.upper(),"Horoscope ============")
# # today horoscope
# today_keys = your_horoscope["today"].keys()
# if (len(today_keys) > 1):
#   print("\n************ Today's Horoscope ************")
#   for key in today_keys:
#     print(key , " - " ,  your_horoscope["today"][key].strip() )

# # tomorrow horoscope
# tomorrow_keys = your_horoscope["tomorrow"].keys()
# if (len(tomorrow_keys) > 1):
#   print("\n************ Tomorrow's Horoscope ************")
#   for key in tomorrow_keys:
#     print(key , " - " ,  your_horoscope["tomorrow"][key].strip() )


# # yesterday horoscope
# yesterday_keys = your_horoscope["yesterday"].keys()
# if (len(yesterday_keys) > 1):
#   print("\n************ Yesterday's Horoscope ************")
#   for key in yesterday_keys:
#     print(key , " - " ,  your_horoscope["yesterday"][key].strip() )


# # week horoscope
# weekly_keys = your_horoscope["weekly"].keys()
# if (len(weekly_keys) > 1):
#   print("\n************ This week's Horoscope ************")
#   for key in weekly_keys:
#     print(key , " - " ,  your_horoscope["weekly"][key].strip() )



# # month horoscope
# month_keys = your_horoscope["month"].keys()
# if (len(month_keys) > 1):
#   print("\n************ This month's Horoscope ************")
#   for key in month_keys:
#     print("\n",key , " - " )
#     for keyhr in your_horoscope["month"][key] :
#       print("->" ,keyhr)




# # year horoscope
# year_keys = your_horoscope["year"].keys()
# if (len(year_keys) > 1):
#   print("\n************ This year's Horoscope ************")
#   for key in year_keys:
#     print("\n",key , " - " )
#     for keyhr in your_horoscope["year"][key] :
#       print("->" ,keyhr)