function CSVtoMat(filename,folder)

Data=readmatrix([folder,'\',filename,'.csv']);

Header=readcell([folder,'\',filename,'.csv']);
Num=sum(cellfun(@sum, cellfun(@ismissing, Header(:,end), 'UniformOutput', false)));

Data=Data(end+1-Num:end,:);
RowNames=Header(1:size(Header,1)-size(Data,1),end);
Header=Header(1:size(Header,1)-size(Data,1),1:end-1);

for ii=1:size(Header,2)
    if ~sum(ismissing(Header{1,ii})) && ~strcmp(Header{1,ii},'Wafer')
        if strcmp(Header{end,ii},'Voltage (V)')
%             if exist('Summary.(Header{1,ii}).(Header{2,ii}).(Header{3,ii}).(Header{4,ii}).Voltage','var')
            if exist('Summary','var') && isfield(Summary,Header{1,ii}) && isfield(Summary.(Header{1,ii}),Header{2,ii}) && ...
                    isfield(Summary.(Header{1,ii}).(Header{2,ii}),Header{3,ii}) && isfield(Summary.(Header{1,ii}).(Header{2,ii}).(Header{3,ii}),Header{4,ii}) ...
                    && isfield(Summary.(Header{1,ii}).(Header{2,ii}).(Header{3,ii}).(Header{4,ii}),'Voltage')
                Column=size(Summary.(Header{1,ii}).(Header{2,ii}).(Header{3,ii}).(Header{4,ii}).Voltage,2);
            else
                Column=0;
            end
            Summary.(Header{1,ii}).(Header{2,ii}).(Header{3,ii}).(Header{4,ii}).Voltage(:,Column+1)=Data(:,ii);
        elseif strcmp(Header{end,ii},'Current (A)')
%             if exist('Summary.(Header{1,ii}).(Header{2,ii}).(Header{3,ii}).(Header{4,ii}).Current','var')
            if exist('Summary','var') && isfield(Summary,Header{1,ii}) && isfield(Summary.(Header{1,ii}),Header{2,ii}) && ...
                    isfield(Summary.(Header{1,ii}).(Header{2,ii}),Header{3,ii}) && isfield(Summary.(Header{1,ii}).(Header{2,ii}).(Header{3,ii}),Header{4,ii}) ...
                    && isfield(Summary.(Header{1,ii}).(Header{2,ii}).(Header{3,ii}).(Header{4,ii}),'Current')
                
                Column=size(Summary.(Header{1,ii}).(Header{2,ii}).(Header{3,ii}).(Header{4,ii}).Current,2);
            else
                Column=0;
            end
            Summary.(Header{1,ii}).(Header{2,ii}).(Header{3,ii}).(Header{4,ii}).Current(:,Column+1)=Data(:,ii);
        end
        for jj=1:size(Header,1)-6
            Summary.(Header{1,ii}).(Header{2,ii}).(Header{3,ii}).(Header{4,ii}).Parameters.(RowNames{4+jj}){Column+1}=Header{4+jj,ii};
        end
        Summary.(Header{1,ii}).(Header{2,ii}).(Header{3,ii}).(Header{4,ii}).Comments=Header{end-1,ii};
    end
end
save([folder,'\',filename,'.mat'],'Summary')
end