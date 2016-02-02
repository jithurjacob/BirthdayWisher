import sqlite3
import w10
import sms


def main():
	con=sqlite3.connect('birthday.db',timeout=1)
	query="select * from birthdays where valid=1 and  strftime('%m-%d', dob)=strftime('%m-%d', date()) "
	data =con.execute(query)
	for row in data:
		print row

		try:
			msg="Happy Birthday D"
			if row[5]=="Male":
				msg+="a"
			sms.send_sms(msg,str(row[4]))
			w10.notify("Boss Today is Birthday of {} I've send your greetings".format(row[1]))
		except Exception, e:
			print e
			w10.notify("Boss Today is Birthday of {} I've failed to send your greetings Sorry :(".format(row[1]))

		

if __name__ == '__main__':
	main()