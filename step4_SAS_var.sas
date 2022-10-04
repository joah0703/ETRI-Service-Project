/*주의분산*/
proc import datafile="F:\2020\study\03_운전자\SAS_VAR분석\구간나눈데이터\P23_350_0.8_주의분산.csv"
	dbms=csv
	out=p27_1;
	getnames=Yes;
run;

data p27_1_var;
	options obs=48659; /*첫번째 관측치부터 (구간 시작-1)까지*/
	set p27_1;
run;

proc varmax data=p27_1_var;
	model  up down left right eye mouth  /p=2;
	output lead=112;
run; 


/*피로*/
proc import datafile="F:\2020\study\03_운전자\SAS_VAR분석\구간나눈데이터\P23_350_0.8_피로.csv"
	dbms=csv
	out=p27_2;
	getnames=Yes;
run;

data p27_2_var;
	options obs=49967; /*첫번째 관측치부터 (구간 시작-1)까지*/
	set p27_2;
run;

proc varmax data=p27_2_var;
	model  up  down left  right eye mouth /p=2;
	output lead=92;
run; 


/*졸음*/
proc import datafile="F:\2020\study\03_운전자\SAS_VAR분석\구간나눈데이터\P23_350_0.8_졸음.csv"
	dbms=csv
	out=p23_3;
	getnames=Yes;
run;

data p23_3_var;
	options obs=38459; /*첫번째 관측치부터 (구간 시작-1)까지*/
	set p23_3;
run;

proc varmax data=p23_3_var;
	model up down   right eye mouth /p=2;
	output lead=3540;
run; 
