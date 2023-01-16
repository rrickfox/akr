eingefahrenWB1 = [
    [7.4 7.3]
    [8.5 8.6]
    [9.8 9.9]
    [12.5 12.7]
    [19.2 18.8]
    [31.1 30.1]
    [52.3 52]
];

ausgefahrenWB1 = [
    [9.3 9.6]
    [10.8 10.6]
    [13.7 13.9]
    [18.5 18.3]
    [36.8 36.4]
    [87.4 88.6]
];

eingefahrenWB2 = [
    [6.9 6.6]
    [8.2 7.8]
    [9.1 9.2]
    [11.9 11.6]
    [17.8 18.4]
    [28.5 29.1]
    [49.6 49.2]
];

ausgefahrenWB2 = [
    [10.4 10.3]
    [11.9 11.5]
    [14.8 15.2]
    [21.5 20.8]
    [40.8 41.3]
    [96.7 99.3]
];

% calculate mean of both measurements

avgAusWB2 = mean(ausgefahrenWB2,2);
avgEinWB2 = mean(eingefahrenWB2,2);
avgAusWB1 = mean(ausgefahrenWB1,2);
avgEinWB1 = mean(eingefahrenWB1,2);

% calculate relative N_0/N_i

relAusWB1 = avgAusWB1(1,:)./avgAusWB1;
relEinWB1 = avgEinWB1(1,:)./avgEinWB1;
relAusWB2 = avgAusWB2(1,:)./avgAusWB2;
relEinWB2 = avgEinWB2(1,:)./avgEinWB2;

xAus = [0 100 200 300 400 450];
xEin = [xAus 500]

figure
subplot(2,1,1);
plot(xAus, relAusWB1);
hold on
plot(xEin, relEinWB1);
title('WB1')
legend({'ausgefahren' 'eingefahren'})
ylim([0 1]);
xlim([0 800]);


subplot(2,1,2);
plot(xAus, relAusWB2);
hold on
plot(xEin, relEinWB2);
title('WB2')
legend({'ausgefahren' 'eingefahren'})
ylim([0 1]);
xlim([0 800]);

