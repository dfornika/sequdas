######################################################################
#								     #
# sequdas pipeline runner                                            #
#	                                 			     #
# Version 1.4							     #
#								     #
# 2017-11-21							     #
#								     #
# Jun Duan                                                           #
# BCCDC Public Health Laboratory                                     #
# University of British Columbia                                     #
# duanjun1981@gmail.com                                              #
#                                                                    #
# William Hsiao, PhD                                                 #
# Senior Scientist (Bioinformatics), BCCDC Public Health Laboratory  #
# Clinical Assistant Professor, Pathology & Laboratory Medicine, UBC #
# Adjunct Professor, Molecular Biology and Biochemistry, SFU         #
# Rm 2067a, 655 West 12th Avenue                                     #
# Vancouver, BC, V5Z 4R4                                             #
# Canada                                                             #
# Tel: 604-707-2561                                                  #
# Fax: 604-707-2603                                                  #
#                                                                    #
######################################################################

import sys
import re
import shutil
import zerorpc
import sequdas_server.core

def _main(argv):
    (input_dir, out_dir, step_id, run_style, keep_kraken) = run_parameter(argv)
    run_style = str2bool(run_style)
    keep_kraken = str2bool(keep_kraken)
    run_folder_name = os.path.basename(os.path.normpath(input_dir))
    run_analysis_folder = out_dir + "/" + run_folder_name
    check_folder(out_dir)
    check_folder(run_analysis_folder)
    step_id = int(step_id)    
    if(step_id == 1):
        run_machine_QC(input_dir, out_dir)
        copy_reporter(out_dir, run_folder_name)
        if run_style is True:
            step_id += 1
    if(step_id == 2):
        run_fastqc(input_dir, out_dir)
        copy_reporter(out_dir, run_folder_name)
        if run_style is True:
            step_id += 1
    if(step_id == 3):
        run_multiQC(input_dir, out_dir)
        copy_reporter(out_dir, run_folder_name)
        if run_style is True:
            step_id += 1            
    if(step_id == 4):
        run_kraken(input_dir, out_dir, keep_kraken)
        copy_reporter(out_dir, run_folder_name)
        if run_style is True:
            step_id += 1
    if(step_id == 5):
        sequdas_server.core.upload_to_irida(input_dir)

class SequdasRPC(object):
    def hello(self, name):
        return "Hello, %s" % name
    def qc(self):
        run_machine_QC(input_dir, out_dir)
        copy_reporter(out_dir, run_folder_name)
    def fastqc(self):
        run_fastqc(input_dir, out_dir)
        copy_reporter(out_dir, run_folder_name)
    def multiqc(self):
        run_multiQC(input_dir, out_dir)
        copy_reporter(out_dir, run_folder_name)
    def kraken(self):
        run_kraken(input_dir, out_dir, keep_kraken)
        copy_reporter(out_dir, run_folder_name)
    def irida_upload(self):
        sequdas_server.core.upload_to_irida(input_dir)

def main(argv):
    (input_dir, out_dir, step_id, run_style, keep_kraken) = sequdas_server.core.run_parameter(argv)
    run_style = str2bool(run_style)
    keep_kraken = str2bool(keep_kraken)
    run_folder_name = os.path.basename(os.path.normpath(input_dir))
    run_analysis_folder = out_dir + "/" + run_folder_name
    check_folder(out_dir)
    check_folder(run_analysis_folder)
    
    s = zerorpc.Server(SequdasRPC())
    s.bind("tcp://0.0.0.0:4242")
    s.run()

if __name__ == "__main__":
    main(sys.argv[1:])
