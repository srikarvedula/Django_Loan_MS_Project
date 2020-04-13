create database loan_proj;
use loan_proj;

create table loan_table_lookup(
	loan_mdm_lookup_id	int
,CreditScoreMin			int
,CreditScoreMax			int
,LoanAmountMin			int
,LoanAmountMax			int
,InterestRatePct		decimal(4,2)
,DurationMonths			int
,eff_from_date			date
,eff_to_date			date
);

alter table loan_table_lookup add constraint loan_table_lookup_pk primary key(loan_mdm_lookup_id);

select * from loan_table_lookup;