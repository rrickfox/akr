data = [
    0.5 24505 23967 24063 23525 11971 11433
    1.0 21163 20625 22350 21812 11134 10596
    1.5 18339 17801 20668 20130 10651 10113
    2.0 15840 15302 19868 19330 10252 10113
    2.5 13718 13180 18376 17838 9285  8747 
    3.0 11656 11118 17582 17044 8809  8271 
    3.5 10279 9741  16477 15939 8314  7776 
    4.0 8744  8206  15461 14923 8117  7579 
    4.5 7612  7074  14629 14097 7423  6885 
    5.0 6536  5998  13838 13300 7081  6543 
    5.5 5961  5423  12893 12355 6791  6253 
    6.0 5102  4564  12004 11466 6380  5842 
    6.5 4426  3888  11673 11135 6026  5488 
    7.0 3948  3410  11196 10658 5638  5100 
    7.5 3381  2843  10355 9817  5410  4872 
    8.0 3060  2522  10077 9539  5180  4642 
    8.5 2691  2153  9477  8939  4852  4314 
    9.0 2300  1762  9009  8471  4645  4107 
    10.0 1930 1392 8152 7614 4096 3558
];

%% reformat data

x = data(:,1);
y1 = data(:,3);
y2 = data(:,5);
y3 = data(:,7);
err1 = sqrt(y1);
err2 = sqrt(y2);
err3 = sqrt(y3);

%% Normal

t1 = tiledlayout(1,1,'Padding','tight');
t1.Units = 'inches';
t1.OuterPosition = [0.25 0.25 6 4];
nexttile;

errorbar(x,y1,err1);
hold on;
errorbar(x,y2,err2);
hold on;
errorbar(x,y3,err3);

title('Zerfälle in Abhängigkeit der Zeit');
xlabel('Zeit [min]');
ylabel('Zerfälle innerhalb 6s [Bq]');
legend('Al','Cu','X');

axis padded;
grid on;

exportgraphics(t1,'linear.png','Resolution',500)

%% Logarithmic

t2 = tiledlayout(1,1,'Padding','tight');
t2.Units = 'inches';
t2.OuterPosition = [0.25 0.25 6 4];
nexttile;

errorbar(x,y1,err1);
hold on;
errorbar(x,y2,err2);
hold on;
errorbar(x,y3,err3);

title('Zerfälle in Abhängigkeit der Zeit');
xlabel('Zeit [min]');
ylabel('Zerfälle innerhalb 6s [Bq]');
legend('Al','Cu','X');

set(gca, ...
    'YScale','log', ...
    'YLim',[1e3 2.5e4], ...
    'XLim',[0 10.5]);

grid on;

exportgraphics(t2,'logarithmic.png','Resolution',500)

clc;