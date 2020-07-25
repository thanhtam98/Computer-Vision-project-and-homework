clc;clear all;close all;

weight=rand(50,1)*3;
lenght1=rand(50,1)*6;
rabbit=[weight lenght1];

weight=rand(50,1)*4+1.5;
lenght1=rand(50,1)*5+2;
dog=[weight lenght1];

% All the training data
dfeat=[rabbit;dog];
dclass(1:50)=-1; dclass(51:100)=1;

figure, subplot(2,2,1), hold on; axis equal;
plot(rabbit(:,1),rabbit(:,2),'g*'); plot(dog(:,1),dog(:,2),'k.');
title('Training Data');
xlabel('weight');
ylabel('lenght');
 % Adaboost to make a classifier
[cestimate,model]=adaboost('train',dfeat,dclass,70);
 % Results
 rabbit=dfeat(cestimate==-1,:); dog=dfeat(cestimate==1,:);
I=zeros(161,161);
 for i=1:length(model)
     if(model(i).dimension==1)
        if(model(i).direction==1), rec=[-80 -80 80+model(i).threshold 160];
        else rec=[model(i).threshold -80 80-model(i).threshold 160 ];
         end
     else
        if(model(i).direction==1), rec=[-80 -80 160 80+model(i).threshold];
        else rec=[-80 model(i).threshold 160 80-model(i).threshold];
         end
     end
     rec=round(rec);
     y=rec(1)+81:rec(1)+81+rec(3); x=rec(2)+81:rec(2)+81+rec(4);
     I=I-model(i).alpha; I(x,y)=I(x,y)+2*model(i).alpha;
 end
 subplot(2,2,2), imshow(I,[]); colorbar; axis xy;
colormap('jet'), hold on
plot(rabbit(:,1)+81,rabbit(:,2)+81,'bo');
plot(dog(:,1)+81,dog(:,2)+81,'ro');
title('Training Data classified with adaboost model');
error=zeros(1,length(model)); for i=1:length(model), error(i)=model(i).error; end
subplot(2,2,3), plot(error);
xlabel('number  of weak classifiers')
ylabel('error')
% Make some test data
weight=rand(50,1)*7; lenght1=rand(50,1)*5; test=[weight lenght1];
% Classify the testdata with the trained model
testclass=adaboost('apply',test,model);
% Show result
rabbit=test(testclass==-1,:); dog=test(testclass==1,:);
% Show the data
subplot(2,2,4), hold on
plot(rabbit(:,1),rabbit(:,2),'go');
plot(dog(:,1),dog(:,2),'ko');
axis equal;
title('Testing new model');
%   User data
weight=input('Introduce the weight ');
lenght1=input('Introduce the lenght ');
tuser=[weight lenght1];
testuser=adaboost('apply',tuser,model);
% Show result
rabbit=tuser(testuser==-1,:); dog=tuser(testuser==1,:);
plot(rabbit(:,1),rabbit(:,2),'gx','LineWidth',2);
plot(dog(:,1),dog(:,2),'kx','LineWidth',2);
