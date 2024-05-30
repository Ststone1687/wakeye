import flask
from flask import Flask, render_template, request
from replit import db
app = flask.Flask(__name__)
#print(db["rank"])
#print(db["Users"].keys())
#print(db["Users"])
#KEYS = db["rank"].keys()
#DATA = db["Users"]
#for i in KEYS:
#if(DATA[str(i)][3]<=0.2):
#del DATA[str(i)]
#db["rank"] = DATA
#del db["Users"]["ㅤ"]
#del DATA["ㅤ"]
#db["Users"]=DATA
#db["polar"]={}


@app.route('/creat/', methods=['GET', 'POST'])
def test():
	if request.method == 'POST' and "send" in flask.request.form:
		User = request.form.get('User_name')
		key = request.form.get('key')
		password1 = request.form.get('password1')
		password2 = request.form.get('password2')
		L = db["Users"].keys()
		ad = db["Users"]
		if (str(key) != "66666"):
			return '<a href="https://tiantian.guaichi.repl.co/">金鑰不對</a>'
		elif (str(User) in str(L)):
			return '<a href="https://tiantian.guaichi.repl.co/">此使用者帳號無法使用</a>'
		elif (str(password1) != str(password2)):
			return '<a href="https://tiantian.guaichi.repl.co/">確認密碼錯誤</a>'
		elif (" " in str(password1) or " " in str(User)
		      or "ㅤ" in str(password1) or "ㅤ" in str(User)):
			return '<a href="https://tiantian.guaichi.repl.co/">帳號或密碼中不得有空格</a>'
		else:
			ad[str(User)] = [password1]
			db["Users"] = ad
		return '<a href="https://tiantian.guaichi.repl.co/">創建成功</a>'
	return flask.render_template('creat.html')  #i love you tiantian


@app.route('/', methods=['GET', 'POST'])
def ten_sec_contest():
	if request.method == 'POST' and "record" in flask.request.form:
		User = request.form.get('sname')
		PASS = request.form.get('spass')
		L = db["Users"].keys()
		ad = db["Users"]
		#print(User)
		#print(PASS)
		COR = int(request.form.get('COR'))
		INC = int(request.form.get('INC'))
		if (COR * 10 / (COR + INC) <= 2):
			return '<a href="https://tiantian.guaichi.repl.co/">你的答對率太低了喔</a>'
		elif (str(User) in str(L)):
			if (ad[str(User)][0] != str(PASS)):
				return '<a href="https://tiantian.guaichi.repl.co/">密碼錯誤</a>'
			else:
				COR = int(request.form.get('COR'))
				INC = int(request.form.get('INC'))
				UNA = int(request.form.get('UNA'))
				#score = flask.request.form['User_name']
				KEYS = db["rank"].keys()
				rank = db["rank"]
				flag = "f"
				for n in KEYS:
					if (str(n) == str(User)):
						flag = "t"
						if (COR > int(rank[str(User)][0]) or (COR == int(rank[str(User)][0]) and INC < int(rank[str(User)][1]))):
							rank[str(User)][0] = COR
							rank[str(User)][1] = INC
							rank[str(User)][2] = UNA
							rank[str(User)][3] = (int(COR) /(int(COR) + int(INC)))
				if (flag == "f"):
					rank[str(User)] = [COR, INC, UNA, (int(COR) / (int(COR) + int(INC))), 0]
				db["rank"] = rank
				#print(score)
				return '<a href="https://tiantian.guaichi.repl.co/">已經更新排行榜，請重新載入</a>'
		else:
			return '<a href="https://tiantian.guaichi.repl.co/">此使用者帳號法使用</a>'
	return flask.render_template('ten_sec_contest.html')


@app.route('/rank/', methods=['GET', 'POST'])
def rank():
	KEYS = db["rank"].keys()
	DATA = db["rank"]
	#print(KEYS)
	for i in KEYS:
		DATA[str(i)][0] = int(DATA[str(i)][0])
	print(KEYS)
	sorted_counts = sorted(DATA.items(), key=lambda x: x[1], reverse=True)
	print(sorted_counts)
	return flask.render_template('rank.html',keys=KEYS,data=DATA,
sorted_counts=sorted_counts)


@app.route('/20xchallengetemplate/', methods=['GET', 'POST'])
def _20xchallengetemplate():
	if request.method == 'POST' and "record" in flask.request.form:
		User = request.form.get('sname')
		PASS = request.form.get('spass')
		L = db["Users"].keys()
		ad = db["Users"]
		#print(User)
		#print(PASS)
		if (str(User) in str(L)):
			if (ad[str(User)][0] != str(PASS)):
				return '<a href="https://tiantian.guaichi.repl.co/20xchallengetemplate/">密碼錯誤</a>'
			else:
				sec = int(request.form.get('sec'))
				score = int(request.form.get('score'))
				#score = flask.request.form['User_name']
				KEYS = db["twenty"].keys()
				rank = db["twenty"]
				flag = "f"
				for n in KEYS:
					if (str(n) == str(User)):
						flag = "t"
						if (sec < int(rank[str(User)][0])
						    or (sec == int(rank[str(User)][0])
						        and score > int(rank[str(User)][1]))):
							rank[str(User)][0] = sec
							rank[str(User)][1] = score
				if (flag == "f"):
					rank[str(User)] = [sec, score, 0, 0, 0]
				db["twenty"] = rank
				#print(score)
				return '<a href="https://tiantian.guaichi.repl.co/20xchallengetemplate/">已經更新排行榜，請重新載入</a>'
		else:
			return '<a href="https://tiantian.guaichi.repl.co/20xchallengetemplate/">此使用者帳號法使用</a>'
	return flask.render_template('20xchallengetemplate.html')


@app.route('/rank_20xchallenge/', methods=['GET', 'POST'])
def rank_20xchallengetemplate():
	KEYS = db["twenty"].keys()
	DATA = db["twenty"]
	#print(KEYS)
	for i in KEYS:
		DATA[str(i)][0] = int(DATA[str(i)][0])
	print(KEYS)
	sorted_counts = sorted(DATA.items(), key=lambda x: x[1])
	print(sorted_counts)
	return flask.render_template('rank_20xchallengetemplate.html',keys=KEYS,data=DATA,sorted_counts=sorted_counts)

@app.route('/polar/',methods=['GET','POST'])
def polar():
  if request.method == 'POST' and "record" in flask.request.form:
    User = request.form.get('sname')
    PASS = request.form.get('spass')
    L = db["Users"].keys()
    ad = db["Users"]
		#print(User)
		#print(PASS)
    COR = int(request.form.get('COR'))
    INC = int(request.form.get('INC'))
    if (COR * 10 / (COR + INC) <= 5):
      return '<a href="https://tiantian.guaichi.repl.co/polar">你的答對率太低了喔</a>'
    elif (str(User) in str(L)):
      if (ad[str(User)][0] != str(PASS)):
        return '<a href="https://tiantian.guaichi.repl.co/polar">密碼錯誤</a>'
      else:
        COR = int(request.form.get('COR'))
        INC = int(request.form.get('INC'))
        #UNA = int(request.form.get('UNA'))
				#score = flask.request.form['User_name']
        KEYS = db["polar"].keys()
        rank = db["polar"]
        flag = "f"
        for n in KEYS:
          if (str(n) == str(User)):
            flag = "t"
            if (COR > int(rank[str(User)][0]) or (COR == int(rank[str(User)][0]) and INC < int(rank[str(User)][1]))):
              rank[str(User)][0] = COR
              rank[str(User)][1] = INC
              #rank[str(User)][2] = UNA
              rank[str(User)][2] = (int(COR) /(int(COR) + int(INC)))
        if (flag == "f"):
          rank[str(User)] = [COR, INC, (int(COR) / (int(COR) + int(INC))), 0,0]
        db["polar"] = rank
				#print(score)
        return '<a href="https://tiantian.guaichi.repl.co/polar">已經更新排行榜，請重新載入</a>'
    else:
      return '<a href="https://tiantian.guaichi.repl.co/polar">此使用者帳號法使用</a>'
  return flask.render_template('polar.html')

@app.route('/polar_rank/', methods=['GET', 'POST'])
def polar_rank():
	KEYS = db["polar"].keys()
	DATA = db["polar"]
	#print(KEYS)
	for i in KEYS:
		DATA[str(i)][0] = int(DATA[str(i)][0])
	print(KEYS)
	sorted_counts = sorted(DATA.items(), key=lambda x: x[1])
	print(sorted_counts)
	return flask.render_template('polar_rank.html',keys=KEYS,data=DATA,sorted_counts=sorted_counts)

@app.route('/home.jp/', methods=['GET', 'POST'])
def home_jp():
  return flask.render_template('/JP/home.html')

@app.route('/beggin.jp/', methods=['GET', 'POST'])
def beggin_jp():
  return flask.render_template('/JP/beggin.html')

@app.route('/trigonometry.jp/', methods=['GET', 'POST'])
def trigonometry_jp():
  return flask.render_template('/JP/trigonometry.html')

@app.route('/20xchallengetemplate.jp/', methods=['GET', 'POST'])
def _20challengetemplate_jp():
  return flask.render_template('/JP/20xchallengetemplate.html')

@app.route('/20xchallengetemplate_second.jp/', methods=['GET', 'POST'])
def _20xchallengetemplate_second_jp():
  if request.method == 'POST' and "record" in flask.request.form:
    User = request.form.get('sname')
    PASS = request.form.get('spass')
    L = db["Users"].keys()
    ad = db["Users"]
		#print(User)
		#print(PASS)
    if (str(User) in str(L)):
      if (ad[str(User)][0] != str(PASS)):
        return '<a href="https://tiantian.guaichi.repl.co/20xchallengetemplate_second.jp/">パスワードエラー</a>'
      else:
        sec = int(request.form.get('sec'))
        score = int(request.form.get('score'))
				#score = flask.request.form['User_name']
        KEYS = db["twenty"].keys()
        rank = db["twenty"]
        flag = "f"
        for n in KEYS:
          if (str(n) == str(User)):
            flag = "t"
            if (sec < int(rank[str(User)][0])or (sec == int(rank[str(User)][0])and score > int(rank[str(User)][1]))):
              rank[str(User)][0] = sec
              rank[str(User)][1] = score
        if (flag == "f"):
          rank[str(User)] = [sec, score, 0, 0, 0]
        db["twenty"] = rank
				#print(score)
        return '<a href="https://tiantian.guaichi.repl.co/20xchallengetemplate_second.jp/">成功</a>'
    else:
      return '<a href="https://tiantian.guaichi.repl.co/20xchallengetemplate_second.jp/">このユーザーは存在しません</a>'
  return flask.render_template('/JP/20xchallengetemplate_second.html')

@app.route('/six_sec_content.jp/', methods=['GET', 'POST'])
def six_sec_content_jp():
  if request.method == 'POST' and "record" in flask.request.form:
    User = request.form.get('sname')
    PASS = request.form.get('spass')
    L = db["Users"].keys()
    ad = db["Users"]
		#print(User)
		#print(PASS)
    COR = int(request.form.get('COR'))
    INC = int(request.form.get('INC'))
    if (COR * 10 / (COR + INC) <= 2):
      return '<a href="/six_sec_content.jp/">正解率は低い</a>'
    elif (str(User) in str(L)):
      if (ad[str(User)][0] != str(PASS)):
        return '<a href="/six_sec_content.jp/">パスワードエラー</a>'
      else:
        COR = int(request.form.get('COR'))
        INC = int(request.form.get('INC'))
        UNA = int(request.form.get('UNA'))
				#score = flask.request.form['User_name']
        KEYS = db["rank"].keys()
        rank = db["rank"]
        flag = "f"
        for n in KEYS:
          if (str(n) == str(User)):
            flag = "t"
            if (COR > int(rank[str(User)][0]) or (COR == int(rank[str(User)][0]) and INC < int(rank[str(User)][1]))):
              rank[str(User)][0] = COR
              rank[str(User)][1] = INC
              rank[str(User)][2] = UNA
              rank[str(User)][3] = (int(COR) /(int(COR) + int(INC)))
        if (flag == "f"):
          rank[str(User)] = [COR, INC, UNA, (int(COR) / (int(COR) + int(INC))), 0]
        db["rank"] = rank
				#print(score)
        return '<a href="/six_sec_content.jp/">成功</a>'
    else:
      return '<a href="/six_sec_content.jp/">このユーザーは存在しません</a>'
  return flask.render_template('/JP/six_sec_content.html')

@app.route('/polar.jp/', methods=['GET', 'POST'])
def polar_jp():
  return flask.render_template('/JP/polar.html')

@app.route('/polar_second.jp/', methods=['GET', 'POST'])
def polar_second_jp():
  if request.method == 'POST' and "record" in flask.request.form:
    User = request.form.get('sname')
    PASS = request.form.get('spass')
    L = db["Users"].keys()
    ad = db["Users"]
		#print(User)
		#print(PASS)
    COR = int(request.form.get('COR'))
    INC = int(request.form.get('INC'))
    if (COR * 10 / (COR + INC) <= 5):
      return '<a href="/polar_second.jp/">正解率は低い</a>'
    elif (str(User) in str(L)):
      if (ad[str(User)][0] != str(PASS)):
        return '<a href="/polar_second.jp/">パスワードエラー</a>'
      else:
        COR = int(request.form.get('COR'))
        INC = int(request.form.get('INC'))
        #UNA = int(request.form.get('UNA'))
				#score = flask.request.form['User_name']
        KEYS = db["polar"].keys()
        rank = db["polar"]
        flag = "f"
        for n in KEYS:
          if (str(n) == str(User)):
            flag = "t"
            if (COR > int(rank[str(User)][0]) or (COR == int(rank[str(User)][0]) and INC < int(rank[str(User)][1]))):
              rank[str(User)][0] = COR
              rank[str(User)][1] = INC
              #rank[str(User)][2] = UNA
              rank[str(User)][2] = (int(COR) /(int(COR) + int(INC)))
        if (flag == "f"):
          rank[str(User)] = [COR, INC, (int(COR) / (int(COR) + int(INC))), 0,0]
        db["polar"] = rank
				#print(score)
        return '<a href="/polar_second.jp/">成功入</a>'
    else:
      return '<a href="/polar_second.jp/">このユーザーは存在しません</a>'
  return flask.render_template('/JP/polar_second.html')

@app.route('/rank.jp/', methods=['GET', 'POST'])
def rank_jp():
	KEYS = db["rank"].keys()
	DATA = db["rank"]
	#print(KEYS)
	for i in KEYS:
		DATA[str(i)][0] = int(DATA[str(i)][0])
	print(KEYS)
	sorted_counts = sorted(DATA.items(), key=lambda x: x[1], reverse=True)
	print(sorted_counts)
	return flask.render_template('/JP/rank.html',keys=KEYS,data=DATA,
sorted_counts=sorted_counts)

@app.route('/rank_20xchallenge.jp/', methods=['GET', 'POST'])
def rank_20xchallengetemplate_jp():
	KEYS = db["twenty"].keys()
	DATA = db["twenty"]
	#print(KEYS)
	for i in KEYS:
		DATA[str(i)][0] = int(DATA[str(i)][0])
	print(KEYS)
	sorted_counts = sorted(DATA.items(), key=lambda x: x[1])
	print(sorted_counts)
	return flask.render_template('/JP/rank_20xchallengetemplate.html',keys=KEYS,data=DATA,sorted_counts=sorted_counts)

@app.route('/polar_rank.jp/', methods=['GET', 'POST'])
def polar_rank_jp():
	KEYS = db["polar"].keys()
	DATA = db["polar"]
	#print(KEYS)
	for i in KEYS:
		DATA[str(i)][0] = int(DATA[str(i)][0])
	print(KEYS)
	sorted_counts = sorted(DATA.items(), key=lambda x: x[1])
	print(sorted_counts)
	return flask.render_template('/JP/polar_rank.html',keys=KEYS,data=DATA,sorted_counts=sorted_counts)

@app.route('/credits.jp/', methods=['GET', 'POST'])
def credits_jp():
  return flask.render_template('/JP/credits.html')

@app.route('/create.jp/', methods=['GET', 'POST'])
def creat_jp():
	if request.method == 'POST' and "send" in flask.request.form:
		User = request.form.get('User_name')
		key = request.form.get('key')
		password1 = request.form.get('password1')
		password2 = request.form.get('password2')
		L = db["Users"].keys()
		ad = db["Users"]
		if (str(key) != "66666"):
			return '<a href="/home.jp/">キーは違う</a>'
		elif (str(User) in str(L)):
			return '<a href="/home.jp/">このユーザーアカウントは利用できません</a>'
		elif (str(password1) != str(password2)):
			return '<a href="/home.jp/">パスワードエラー</a>'
		elif (" " in str(password1) or " " in str(User)
		      or "ㅤ" in str(password1) or "ㅤ" in str(User)):
			return '<a href="/home.jp/">スペースが禁止</a>'
		else:
			ad[str(User)] = [password1]
			db["Users"] = ad
		return '<a href="https://tiantian.guaichi.repl.co/">成功</a>'
	return flask.render_template('/JP/create.html')  #i love you tiantian

app.run('0.0.0.0')