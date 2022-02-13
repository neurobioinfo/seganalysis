import os 
# import sys
import pandas as pd 
import numpy as np
from statistics import mode
import itertools 

def sub_seg(outfolder, header_need):
    """
    outfolder: the folder that you want to save your output 
    header_need: the header that you want. 
    """
    # header_fin_name=f'{outfolder}/header.txt'    
    # header_fin=pd.read_csv(header_fin_name, sep='\t',index_col=False,header=None)
    header_need_name=f'{header_need}'            
    header_need=pd.read_csv(header_need_name, sep='\t',index_col=False,header=None)
    final_name=f'{outfolder}/finalseg.csv'        
    final=pd.read_csv(final_name, sep='\t',index_col=False)
    header_fin=list(final.columns)   
    list2=[header_fin.index(i) for i in header_need.iloc[0,:].tolist()]
    list2=list(set(list2))
    def uniq_unsort(x):
        indexes = np.unique(x, return_index=True)[1]
        return ([x[index] for index in sorted(indexes)])
    def gen_unique(x):
        xset = list(uniq_unsort(x))
        res0='|'.join(xset)
        return(res0)
    def run_unique(x):
        res=x.apply(gen_unique)
        return(res)
    final2=final.iloc[:,list2]
    for i in list(np.where(final2.dtypes=='object')[0]):
        if i==0: continue 
        try: 
            final2.iloc[:,i] = final2.iloc[:,i].apply(eval)
        except (SyntaxError, NameError, TypeError, ZeroDivisionError):    
            pass
        final2.iloc[:,i]=run_unique(final2.iloc[:,i])
    final2_name=f'{outfolder}/finalseg_modified.csv'        
    final2.to_csv(final2_name,index=False)
    cmd_prune=f'cd {outfolder}; sed -i finalseg_modified.csv -e "s/,|/,/g" -e "s/|,/,/g"'
    os.system(cmd_prune)


# the following function calculate the mean and mode 
def clean_seg_calculate_mean_mode(outfolder, header_need, header_to_modify):
    header_fin_name=f'{outfolder}/header.txt'    
    header_fin=pd.read_csv(header_fin_name, sep='\t',index_col=False,header=None)
    header_need_name=f'{outfolder}/{header_need}'            
    header_need=pd.read_csv(header_need_name, sep='\t',index_col=False,header=None)
    header_abs_name=f'{outfolder}/{header_to_modify}'    
    header_abs=pd.read_csv(header_abs_name, sep='\t',index_col=False,header=None)
    final_name=f'{outfolder}/finalseg.csv'        
    final=pd.read_csv(final_name, sep='\t',index_col=False)
    def floatB(aa):
        try:
            res=float(aa)
        except ValueError as err:
            res=np.NaN
        return(res)
    def con_float(x):
        res0=[floatB(s) for s in x]
        return(np.nanmean(res0))
    def check_is_numberic(x):
        ab=x[1:10].tolist()
        merged = list(itertools.chain(*ab))
        ac=list(filter(None, merged))
        while len(ac)<1:
            ad0=10
            ab=x[(1+ad0):(10+ad0)].tolist()
            merged = list(itertools.chain(*ab))
            ac=list(filter(None, merged))
        return(all(ele.isdigit() for ele in ac))
    def cal_mode_mean(x):
        if check_is_numberic(x):
            res=x.apply(con_float)
        else:
            res=x.apply(mode)
        return(res)
    list1=[header_fin.iloc[0,:].tolist().index(i) for i in header_abs.iloc[0,:].tolist()]
    list2=[header_fin.iloc[0,:].tolist().index(i) for i in header_need.iloc[0,:].tolist()]
    j_t=header_fin.shape[1]
    for i in list1:
        if i==0: next 
        if isinstance(final.iloc[:,i], object):
            final.iloc[:,i] = final.iloc[:,i].apply(eval)
        j_t=j_t+1
        new_col=final.columns[i]+'modified'
        final[new_col]=cal_mode_mean(final.iloc[:,i])
    new_list = [x+header_fin.shape[1] for x in range(0,len(list1))]
    listt=list2+new_list
    final2=final.iloc[:,listt]
    # final_name=f'{outfolder}finalseg_m.csv'
    # final.iloc[:,listt].to_csv(final_name,index=False)
    for i in range(1,final2.shape[1]):
        # if i==0: next 
        try: 
            final2.iloc[:,i] = final2.iloc[:,i].apply(eval)
        except :
            next
    final2_name=f'{outfolder}/finalseg_modified.csv'        
    final2.to_csv(final2_name,index=False)
    cmd_prune=f'cd {outfolder}; sed -i finalseg_modified.csv -e "s/\'//g"'
    os.system(cmd_prune)



if __name__ == "__main__":
    sub_seg()
