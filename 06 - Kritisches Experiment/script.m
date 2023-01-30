clear all;
set(groot,'defaultLineLineWidth',1.8)
set(groot,'defaultAxesFontSize',14)

c1 = "#0072BD";
c2 = "#EDB120";

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

xAus = [0 100 200 300 400 450];
xEin = [xAus 500];

% calculate mean of both measurements

avgAusWB2 = mean(ausgefahrenWB2,2);
avgEinWB2 = mean(eingefahrenWB2,2);
avgAusWB1 = mean(ausgefahrenWB1,2);
avgEinWB1 = mean(eingefahrenWB1,2);

%% calculate & plot relative N_0/N_i

% calculation

relAusWB1 = avgAusWB1(1,:)./avgAusWB1;
relEinWB1 = avgEinWB1(1,:)./avgEinWB1;
relAusWB2 = avgAusWB2(1,:)./avgAusWB2;
relEinWB2 = avgEinWB2(1,:)./avgEinWB2;

extraAusWB1 = fzero(@(x) interp1([xAus(end-1) xAus(end)],[relAusWB1(end-1) relAusWB1(end)],x,'spline'),450);
extraEinWB1 = fzero(@(x) interp1([xEin(end-1) xEin(end)],[relEinWB1(end-1) relEinWB1(end)],x,'spline'),450);
extraAusWB2 = fzero(@(x) interp1([xAus(end-1) xAus(end)],[relAusWB2(end-1) relAusWB2(end)],x,'spline'),450);
extraEinWB2 = fzero(@(x) interp1([xEin(end-1) xEin(end)],[relEinWB2(end-1) relEinWB2(end)],x,'spline'),450);



% plot

grayColor = [.7 .7 .7];

figure

plot(xEin,relEinWB1,"--",'color',c1);
hold on
plot(xAus,relAusWB1,'color',c1);
hold on
plot(xEin,relEinWB2,"--",'color',c2);
hold on
plot(xAus,relAusWB2,'color',c2);
hold on
plot([xAus(end) extraAusWB1],[relAusWB1(end) 0],'color',grayColor);
hold on
plot([xAus(end) extraAusWB2],[relAusWB2(end) 0],'color',grayColor);
hold on
plot([xEin(end) extraEinWB1],[relEinWB1(end) 0],'color',grayColor);
hold on
plot([xEin(end) extraEinWB2],[relEinWB2(end) 0],'color',grayColor);


legend({'WB1 eingefahren' 'WB1 ausgefahren' 'WB2 eingefahren' 'WB2 ausgefahren' 'lineare Extrapolation'},Location='northeast');

xlabel('Hubhöhe [digits]');
xticks([0   100   200   300   400   500   508   600])
xticklabels({'0','100','200','300','400', '', 'H_{max} = 508', '600'})

ylabel('N_0/N_i');
ylim([0 1]);
xlim([0 600]);
grid on;

f1 = gcf;
exportgraphics(f1,'relativeCount.eps','Resolution',300)


%% calculate & plot Multiplikationsfaktor k(x)

% calculation

k0 = 0.945;

kEinWB1 = zeros(7,1);
kEinWB1(1) = k0;
kAusWB1 = zeros(6,1);
kAusWB1(1) = k0;
kEinWB2 = zeros(7,1);
kEinWB2(1) = k0;
kAusWB2 = zeros(6,1);
kAusWB2(1) = k0;

for index = 2:length(kEinWB1)
    kEinWB1(index) = 1 + (avgEinWB1(index-1)/avgEinWB1(index)) * (kEinWB1(index-1) - 1);
    kEinWB2(index) = 1 + (avgEinWB2(index-1)/avgEinWB2(index)) * (kEinWB2(index-1) - 1);
end

for index = 2:length(kAusWB1)
    kAusWB1(index) = 1 + (avgAusWB1(index-1)/avgAusWB1(index)) * (kAusWB1(index-1) - 1);
    kAusWB2(index) = 1 + (avgAusWB2(index-1)/avgAusWB2(index)) * (kAusWB2(index-1) - 1);
end

% plot

figure

plot(xEin,kEinWB1,"--",'color',c1);
hold on
plot(xAus,kAusWB1,'color',c1);
hold on
plot(xEin,kEinWB2,"--",'color',c2);
hold on
plot(xAus,kAusWB2,'color',c2);
legend({'WB1 eingefahren' 'WB1 ausgefahren' 'WB2 eingefahren' 'WB2 ausgefahren'},Location='northwest');
ylabel('Multiplikationsfaktor k');
xlabel('Hubhöhe [digits]');
ylim([0.945 1])
xlim([0 550])
grid on;

f2 = gcf;
exportgraphics(f2,'multiplikationsfaktor.eps','Resolution',300)


%% calculate & plot unterkritische Verstärkung M(x)

% calculation

mEinWB1 = 1./(1-kEinWB1(:));
mAusWB1 = 1./(1-kAusWB1(:));
mEinWB2 = 1./(1-kEinWB2(:));
mAusWB2 = 1./(1-kAusWB2(:));

% plot

figure

plot(xEin,mEinWB1,"--",'color',c1);
hold on
plot(xAus,mAusWB1,'color',c1);
hold on
plot(xEin,mEinWB2,"--",'color',c2);
hold on
plot(xAus,mAusWB2,'color',c2);
legend({'WB1 eingefahren' 'WB1 ausgefahren' 'WB2 eingefahren' 'WB2 ausgefahren'},Location='northwest');
ylabel('unterkritische Verstärkung M');
xlabel('Hubhöhe [digits]');
ylim([0 180]);
xlim([0 520]);
grid on;

f3 = gcf;
exportgraphics(f3,'unterkritischeVerstaerkung.eps','Resolution',300)


%% calculate & plot Reaktivität p(x)

% calculation

pEinWB1 = (kEinWB1(:) - 1)./kEinWB1(:);
pAusWB1 = (kAusWB1(:) - 1)./kAusWB1(:);
pEinWB2 = (kEinWB2(:) - 1)./kEinWB2(:);
pAusWB2 = (kAusWB2(:) - 1)./kAusWB2(:);

% plot

figure

plot(xEin,pEinWB1,"--",'color',c1);
hold on
plot(xAus,pAusWB1,'color',c1);
hold on
plot(xEin,pEinWB2,"--",'color',c2);
hold on
plot(xAus,pAusWB2,'color',c2);
legend({'WB1 eingefahren' 'WB1 ausgefahren' 'WB2 eingefahren' 'WB2 ausgefahren'},Location='northwest');
ylabel('Reaktivität p [$]');
xlabel('Hubhöhe [digits]');
ylim([-0.06 0]);
xlim([0 520]);
grid on;

f4 = gcf;
exportgraphics(f4,'reaktivitaet.eps','Resolution',300)
