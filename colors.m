function color=colors(number,total,ColorOrder)
%%
if nargin<1
    error('Not enough inputs!')
elseif nargin==1
    ColorOrder=get(groot,'defaultAxesColorOrder');
    ColorOrder=mat2cell(ColorOrder,ones(1,size(ColorOrder,1)),3)'; % order colors in desired order
    total=length(ColorOrder);
elseif nargin==2
    ColorOrder=get(groot,'defaultAxesColorOrder');
    ColorOrder=mat2cell(ColorOrder,ones(1,size(ColorOrder,1)),3)'; % order colors in desired order
elseif nargin==3 && length(ColorOrder)==1
    ColorOrder=[ColorOrder,ColorOrder];
elseif nargin>3
    error('Too many inputs!')
end

%%
colors=cell([1,length(ColorOrder)]);
for ii=1:length(ColorOrder)
    col=ColorOrder{ii};
    if strcmp(col,'r') || strcmp(col,'red')
        colors{ii}=[1 0 0];
    elseif strcmp(col,'g') || strcmp(col,'green')
        colors{ii}=[0 1 0];
    elseif strcmp(col,'b') || strcmp(col,'blue')
        colors{ii}=[0 0 1];
    elseif strcmp(col,'y') || strcmp(col,'yellow')
        colors{ii}=[1 1 0];
    elseif strcmp(col,'m') || strcmp(col,'magenta')
        colors{ii}=[1 0 1];
    elseif strcmp(col,'c') || strcmp(col,'cyan')
        colors{ii}=[0 1 1];
    elseif strcmp(col,'k') || strcmp(col,'black')
        colors{ii}=[0 0 0];
    elseif strcmp(col,'w') || strcmp(col,'white')
        colors{ii}=[1 0 0];
    elseif length(col(1,:))==3 && length(col(:,1))==1
        colors{ii}=col;
    else
        error('Wrong color input!')
    end
end

pair=NaN(length(colors)-1,3);
for jj=1:length(colors)-1
    pair(jj,:)=colors{jj+1}-colors{jj};
end

%%
if number>total
    error('Number can''t be greater than the total!')
elseif total<=length(colors)
    color=colors{number};
else
    divisions=(total/(length(colors)-1));
    segment=(number/divisions);
    if rem(segment,1)==0 && segment~=0
        segment=segment-1;
    else
        segment=floor(segment);
    end
    number=number-floor((segment)*divisions)-1;
    n=(1:total-1)/divisions;
    subdivision1=n(n>segment);
    subdivision2=subdivision1(subdivision1<=segment+1);
    subdivision=length(subdivision2);
    color=colors{segment+1}+number*pair(segment+1,:)/subdivision;
end

for ll=1:3
    if color(ll)>1
        color(ll)=1;
    elseif color(ll)<0
        color(ll)=0;
    end
end
