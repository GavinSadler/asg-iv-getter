function AnalyzeIVData(Summary,folder,filename)

%%
Wafers=fieldnames(Summary);
Model=fittype('IL-I0*(exp(b*V)-1)','independent','V');
PC=cell(1,length(Wafers));
PCstd=cell(1,length(Wafers));
Voc=cell(1,length(Wafers));
Vocstd=cell(1,length(Wafers));
FF=cell(1,length(Wafers));
FFstd=cell(1,length(Wafers));
Rs=cell(1,length(Wafers));
Rsstd=cell(1,length(Wafers));
Rsh=cell(1,length(Wafers));
Rshstd=cell(1,length(Wafers));
PCdiff=cell(1,length(Wafers));
PCratpc=cell(1,length(Wafers));

e = actxserver('Excel.Application');
for ii=1:length(Wafers)
    Chips=fieldnames(Summary.(Wafers{ii}));
    PCdiff{ii}=cell(1,length(Chips));
    PCratpc{ii}=cell(1,length(Chips));
    eWorkbook = e.Workbooks.Add;
    eSheets = e.ActiveWorkbook.Sheets;
    AllSteps={};
    for jj=1:length(Chips)
        Steps=fieldnames(Summary.(Wafers{ii}).(Chips{jj}));
        if length(Steps)>length(AllSteps)
            AllSteps=Steps;
        end
        RangeStart=2;
        if jj==1
            PC{ii}=NaN(length(Steps),length(Chips));
            Voc{ii}=NaN(length(Steps),length(Chips));
            FF{ii}=NaN(length(Steps),length(Chips));
            Rs{ii}=NaN(length(Steps),length(Chips));
            Rsh{ii}=NaN(length(Steps),length(Chips));
            eSheets.Item(1).Name='Summary';
        end
        eSheets.Add;
        eSheets.Item(1).Name=Chips{jj};

        figure
        hold on
        NS=numSubplots(length(Steps));
        if length(Steps)>1
            sgtitle([Wafers{ii},' ',Chips{jj}],'Interpreter','none')
        else
            title([Wafers{ii},' ',Chips{jj},' ',Steps{1}],'Interpreter','none')
        end
        for kk=1:length(Steps)
            if isfield(Summary.(Wafers{ii}).(Chips{jj}).(Steps{kk}),'Dark') && isfield(Summary.(Wafers{ii}).(Chips{jj}).(Steps{kk}),'Light')
                DVoltage=Summary.(Wafers{ii}).(Chips{jj}).(Steps{kk}).Dark.Voltage;
                LVoltage=Summary.(Wafers{ii}).(Chips{jj}).(Steps{kk}).Light.Voltage;
                DCurrent=1000.*Summary.(Wafers{ii}).(Chips{jj}).(Steps{kk}).Dark.Current;
                LCurrent=1000.*Summary.(Wafers{ii}).(Chips{jj}).(Steps{kk}).Light.Current;
                % assume start, end, and step voltages are always the same for
                % the same conditions
                DV=mean(DVoltage,2);
                DC=mean(DCurrent,2);
                LV=mean(LVoltage,2);
                LC=mean(LCurrent,2);
                VL0=find(LV==0);
                Sat=round(1.2*find(round(LC,2)==round(min(LC),2),1,'last'))+1;
                Start=min(length(LV),round(2*VL0-Sat));
                try
                    [~,gof]=fit(LV(Sat:Start),LC(Sat:Start),Model,'StartPoint',[1,1,-10]);
                catch
                end
                h(kk)=subplot(NS(1),NS(2),kk);
                if sum(DV(:,1)==0)>1
                    EndPlotIndex=find(DV(:,1)==0,2);
                    EndPlotN=EndPlotIndex(2)-1;
                else
                    EndPlotN=length(DV(:,1));
                end
                plot(DV(1:EndPlotN),DC(1:EndPlotN),LV(1:EndPlotN),LC(1:EndPlotN))
                legend('Dark','Light','Box','off')
                box off
                set(gcf,'color','w')
                xlabel('Voltage (V)')
                ylabel('Current (mA)')
                if length(Steps)>1
                    title(Steps{kk},'Interpreter','none')
                end
                PCTemp=NaN(size(LCurrent,2),1);
                VocTemp=NaN(size(LCurrent,2),1);
                FFTemp=NaN(size(LCurrent,2),1);
                RsTemp=NaN(size(LCurrent,2),1);
                RshTemp=NaN(size(LCurrent,2),1);
                for ll=1:size(LCurrent,2)
                    if sum(LVoltage(:,ll)==0)>1
                        IndexTemp=find(LVoltage(:,ll)==0,2);
                        NumElements=IndexTemp(2)-1;
                    else
                        NumElements=length(LVoltage(:,ll));
                    end
                    PCTemp(ll)=LCurrent(LVoltage(1:NumElements,ll)==0,ll);
                    VocTemp(ll)=LVoltage(abs(LCurrent(1:NumElements,ll))==min(abs(LCurrent(1:NumElements,ll))),ll);
                    FFTemp(ll)=min(prod([LVoltage(1:NumElements,ll) LCurrent(1:NumElements,ll)],2))/(PCTemp(ll)*VocTemp(ll));
                    if gof.rsquare>0.95
                        f=fit(LVoltage(Sat:Start,ll),LCurrent(Sat:Start,ll),Model,'StartPoint',[1,1,-10]);
                        Coefs=coeffvalues(f);
                        RsTemp(ll)=-1*Coefs(3)*Coefs(1)*exp(Coefs(3)*VocTemp(ll));
                        RshTemp(ll)=-1*Coefs(3)*Coefs(1);
                    else 
                        RsTemp(ll)=NaN;
                        RshTemp(ll)=NaN;
                    end
                end
                PC{ii}(kk,jj)=mean(PCTemp);
                PCstd{ii}(kk,jj)=std(PCTemp);
                Voc{ii}(kk,jj)=mean(VocTemp);
                Vocstd{ii}(kk,jj)=std(VocTemp);
                FF{ii}(kk,jj)=mean(FFTemp);
                FFstd{ii}(kk,jj)=std(FFTemp);
                Rs{ii}(kk,jj)=mean(RsTemp);
                Rsstd{ii}(kk,jj)=std(RsTemp);
                Rsh{ii}(kk,jj)=mean(RshTemp);
                Rshstd{ii}(kk,jj)=std(RshTemp);

                Results.(Wafers{ii}).(Chips{jj}).(Steps{kk}).PhotoCurrent.Mean=PC{ii}(kk,jj);
                Results.(Wafers{ii}).(Chips{jj}).(Steps{kk}).PhotoCurrent.Std=PCstd{ii}(kk,jj);
                Results.(Wafers{ii}).(Chips{jj}).(Steps{kk}).Voc.Mean=Voc{ii}(kk,jj);
                Results.(Wafers{ii}).(Chips{jj}).(Steps{kk}).Voc.Std=Vocstd{ii}(kk,jj);
                Results.(Wafers{ii}).(Chips{jj}).(Steps{kk}).FillFactor.Mean=FF{ii}(kk,jj);
                Results.(Wafers{ii}).(Chips{jj}).(Steps{kk}).FillFactor.Std=FFstd{ii}(kk,jj);
                Results.(Wafers{ii}).(Chips{jj}).(Steps{kk}).Rs.Mean=Rs{ii}(kk,jj);
                Results.(Wafers{ii}).(Chips{jj}).(Steps{kk}).Rs.Std=Rsstd{ii}(kk,jj);
                Results.(Wafers{ii}).(Chips{jj}).(Steps{kk}).Rsh.Mean=Rsh{ii}(kk,jj);
                Results.(Wafers{ii}).(Chips{jj}).(Steps{kk}).Rsh.Std=Rshstd{ii}(kk,jj);
            else
                if isfield(Summary.(Wafers{ii}).(Chips{jj}).(Steps{kk}),'Dark')
                    Voltage=Summary.(Wafers{ii}).(Chips{jj}).(Steps{kk}).Dark.Voltage;
                    Current=1000.*Summary.(Wafers{ii}).(Chips{jj}).(Steps{kk}).Dark.Current;
                elseif isfield(Summary.(Wafers{ii}).(Chips{jj}).(Steps{kk}),'Light')
                    Voltage=Summary.(Wafers{ii}).(Chips{jj}).(Steps{kk}).Light.Voltage;
                    Current=1000.*Summary.(Wafers{ii}).(Chips{jj}).(Steps{kk}).Light.Current;
                end
                % assume start, end, and step voltages are always the same for
                % the same conditions
                V=mean(Voltage,2);
                C=mean(Current,2);
                if sum(V==0)>1
                        IndexTemp=find(V==0,2);
                        NumElements=IndexTemp(2)-1;
                    else
                        NumElements=length(V);
                    end
                h(kk)=subplot(NS(1),NS(2),kk);
                plot(V(1:NumElements),C(1:NumElements))
                box off
                set(gcf,'color','w')
                xlabel('Voltage (V)')
                ylabel('Current (mA)')
                if length(Steps)>1
                    title(Steps{kk},'Interpreter','none')
                end
            end
        end
        linkaxes(h,'xy');
        saveas(gcf,[folder,'\',filename,'_',Chips{jj}])
        PCdiff{ii}{jj}=repmat(PC{ii}(:,jj),1,kk)-PC{ii}(:,jj);
        PCratpc{ii}{jj}=100.*(repmat(PC{ii}(:,jj),1,kk)./PC{ii}(:,jj)-1);
        CurrentSheet=eSheets.get('Item',Chips{jj});
        CurrentSheet.Activate;
        ActiveRange=get(e.Activesheet,'Range',['B1:',ProperRange(kk+64+1),'1']);
        ActiveRange.Value=Steps';
        ActiveRange=get(e.Activesheet,'Range',['A1:A',num2str(1+kk)]);
        ActiveRange.Value=['Column - Row';Steps];
        ActiveRange=get(e.Activesheet,'Range',['B2:',ProperRange(kk+64+1),num2str(1+kk)]);
        ActiveRange.Value=PCdiff{ii}{jj};
        offset=5+kk;
        ActiveRange=get(e.Activesheet,'Range',['B',num2str(1+offset),':',ProperRange(kk+64+1),num2str(1+offset)]);
        ActiveRange.Value=Steps';
        ActiveRange=get(e.Activesheet,'Range',['A',num2str(1+offset),':A',num2str(1+kk+offset)]);
        ActiveRange.Value=['Column/Row - 1 (%)';Steps];
        ActiveRange=get(e.Activesheet,'Range',['B',num2str(2+offset),':',ProperRange(kk+64+1),num2str(1+kk+offset)]);
        ActiveRange.Value=PCratpc{ii}{jj};
    end
    CurrentSheet=eSheets.get('Item','Summary');
    CurrentSheet.Activate;
    ActiveRange=get(e.Activesheet,'Range',['C1:',ProperRange(jj+64+2),'1']);
    ActiveRange.Value=Chips';
    ActiveRange=get(e.Activesheet,'Range','A1:B1');
    ActiveRange.MergeCells=1;
    ActiveRange.Value='Mean';
    ActiveRange=get(e.Activesheet,'Range',['B1:B',num2str(kk*9+1)]);
    ActiveRange.Value=[' ';repmat([AllSteps;' '],5,1)];
    ActiveRange=get(e.Activesheet,'Range',['C',num2str(RangeStart),':',ProperRange(jj+64+2),num2str(RangeStart+kk-1)]);
    ActiveRange.Value=PC{ii};
    ActiveRange=get(e.Activesheet,'Range',['A',num2str(RangeStart),':A',num2str(RangeStart+kk-1)]);
    ActiveRange.MergeCells=1;
    ActiveRange.Value='Photocurrent (mA)';
    RangeStart=RangeStart+kk+1;
    ActiveRange=get(e.Activesheet,'Range',['C',num2str(RangeStart),':',ProperRange(jj+64+2),num2str(RangeStart+kk-1)]);
    ActiveRange.Value=Voc{ii};
    ActiveRange=get(e.Activesheet,'Range',['A',num2str(RangeStart),':A',num2str(RangeStart+kk-1)]);
    ActiveRange.MergeCells=1;
    ActiveRange.Value='Voc (V)';
    RangeStart=RangeStart+kk+1;
    ActiveRange=get(e.Activesheet,'Range',['C',num2str(RangeStart),':',ProperRange(jj+64+2),num2str(RangeStart+kk-1)]);
    ActiveRange.Value=FF{ii};
    ActiveRange=get(e.Activesheet,'Range',['A',num2str(RangeStart),':A',num2str(RangeStart+kk-1)]);
    ActiveRange.MergeCells=1;
    ActiveRange.Value='Fill Factor';
    RangeStart=RangeStart+kk+1;
    ActiveRange=get(e.Activesheet,'Range',['C',num2str(RangeStart),':',ProperRange(jj+64+2),num2str(RangeStart+kk-1)]);
    ActiveRange.Value=Rs{ii};
    ActiveRange=get(e.Activesheet,'Range',['A',num2str(RangeStart),':A',num2str(RangeStart+kk-1)]);
    ActiveRange.MergeCells=1;
    ActiveRange.Value='Rs (k\Omega)';
    RangeStart=RangeStart+kk+1;
    ActiveRange=get(e.Activesheet,'Range',['C',num2str(RangeStart),':',ProperRange(jj+64+2),num2str(RangeStart+kk-1)]);
    ActiveRange.Value=Rsh{ii};
    ActiveRange=get(e.Activesheet,'Range',['A',num2str(RangeStart),':A',num2str(RangeStart+kk-1)]);
    ActiveRange.MergeCells=1;
    ActiveRange.Value='Rsh (k\Omega)';

    RangeStart=2;
    ActiveRange=get(e.Activesheet,'Range',[ProperRange(jj+64+2+5),'1:',ProperRange(2*jj+64+2+4),'1']);
    ActiveRange.Value=Chips';
    ActiveRange=get(e.Activesheet,'Range',[ProperRange(jj+64+5),'1:',ProperRange(jj+64+5+1),'1']);
    ActiveRange.MergeCells=1;
    ActiveRange.Value='Std';
    ActiveRange=get(e.Activesheet,'Range',[ProperRange(jj+64+5+1),'1:',ProperRange(jj+64+5+1),num2str(kk*9+1)]);
    ActiveRange.Value=[' ';repmat([AllSteps;' '],5,1)];
    ActiveRange=get(e.Activesheet,'Range',[ProperRange(jj+64+2+5),num2str(RangeStart),':',ProperRange(2*jj+64+2+4),num2str(RangeStart+kk-1)]);
    ActiveRange.Value=PCstd{ii};
    ActiveRange=get(e.Activesheet,'Range',[ProperRange(jj+64+5),num2str(RangeStart),':',ProperRange(jj+64+5),num2str(RangeStart+kk-1)]);
    ActiveRange.MergeCells=1;
    ActiveRange.Value='Photocurrent (mA)';
    RangeStart=RangeStart+kk+1;
    ActiveRange=get(e.Activesheet,'Range',[ProperRange(jj+64+2+5),num2str(RangeStart),':',ProperRange(2*jj+64+2+4),num2str(RangeStart+kk-1)]);
    ActiveRange.Value=Vocstd{ii};
    ActiveRange=get(e.Activesheet,'Range',[ProperRange(jj+64+5),num2str(RangeStart),':',ProperRange(jj+64+5),num2str(RangeStart+kk-1)]);
    ActiveRange.MergeCells=1;
    ActiveRange.Value='Voc (V)';
    RangeStart=RangeStart+kk+1;
    ActiveRange=get(e.Activesheet,'Range',[ProperRange(jj+64+2+5),num2str(RangeStart),':',ProperRange(2*jj+64+2+4),num2str(RangeStart+kk-1)]);
    ActiveRange.Value=FFstd{ii};
    ActiveRange=get(e.Activesheet,'Range',[ProperRange(jj+64+5),num2str(RangeStart),':',ProperRange(jj+64+5),num2str(RangeStart+kk-1)]);
    ActiveRange.MergeCells=1;
    ActiveRange.Value='Fill Factor';
    RangeStart=RangeStart+kk+1;
    ActiveRange=get(e.Activesheet,'Range',[ProperRange(jj+64+2+5),num2str(RangeStart),':',ProperRange(2*jj+64+2+4),num2str(RangeStart+kk-1)]);
    ActiveRange.Value=Rsstd{ii};
    ActiveRange=get(e.Activesheet,'Range',[ProperRange(jj+64+5),num2str(RangeStart),':',ProperRange(jj+64+5),num2str(RangeStart+kk-1)]);
    ActiveRange.MergeCells=1;
    ActiveRange.Value='Rs (k\Omega)';
    RangeStart=RangeStart+kk+1;
    ActiveRange=get(e.Activesheet,'Range',[ProperRange(jj+64+2+5),num2str(RangeStart),':',ProperRange(2*jj+64+2+4),num2str(RangeStart+kk-1)]);
    ActiveRange.Value=Rshstd{ii};
    ActiveRange=get(e.Activesheet,'Range',[ProperRange(jj+64+5),num2str(RangeStart),':',ProperRange(jj+64+5),num2str(RangeStart+kk-1)]);
    ActiveRange.MergeCells=1;
    ActiveRange.Value='Rsh (k\Omega)';
    
    SaveAs(eWorkbook,[folder,'\',filename,'_',Wafers{ii},'_Results.xlsx'])
    eWorkbook.Saved = 1;
    Close(eWorkbook)
    
    if exist('Results','var')
        save([folder,'\',filename,'_',Wafers{ii},'_Results.mat'],'Results')
        clear Results;
    end
end
Quit(e)
delete(e)

