/*���Ǻл�*/
proc import datafile="F:\2020\study\03_������\SAS_VAR�м�\��������������\P23_350_0.8_���Ǻл�.csv"
	dbms=csv
	out=p27_1;
	getnames=Yes;
run;

data p27_1_var;
	options obs=48659; /*ù��° ����ġ���� (���� ����-1)����*/
	set p27_1;
run;

proc varmax data=p27_1_var;
	model  up down left right eye mouth  /p=2;
	output lead=112;
run; 


/*�Ƿ�*/
proc import datafile="F:\2020\study\03_������\SAS_VAR�м�\��������������\P23_350_0.8_�Ƿ�.csv"
	dbms=csv
	out=p27_2;
	getnames=Yes;
run;

data p27_2_var;
	options obs=49967; /*ù��° ����ġ���� (���� ����-1)����*/
	set p27_2;
run;

proc varmax data=p27_2_var;
	model  up  down left  right eye mouth /p=2;
	output lead=92;
run; 


/*����*/
proc import datafile="F:\2020\study\03_������\SAS_VAR�м�\��������������\P23_350_0.8_����.csv"
	dbms=csv
	out=p23_3;
	getnames=Yes;
run;

data p23_3_var;
	options obs=38459; /*ù��° ����ġ���� (���� ����-1)����*/
	set p23_3;
run;

proc varmax data=p23_3_var;
	model up down   right eye mouth /p=2;
	output lead=3540;
run; 
