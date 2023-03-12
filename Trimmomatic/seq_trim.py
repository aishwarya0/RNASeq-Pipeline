import sys
import os
import subprocess
import logging
import re
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s", datefmt="%m-%d-%Y %H:%M:%S %Z")
logger = logging.getLogger(__name__)
VERSION = 'V1.0.0'
AUTHOR = 'AUTHOR: Aishwarya Rane, aishwaryarane08@gmail.com, 12/03/2023'
DESCRIPTION = 'Script trims NGS seqeunces'
logger.info(VERSION)
logger.info(AUTHOR)
logger.info(DESCRIPTION)
def run_job(cmd):
    try:
        subprocess.check_call(cmd, shell=True)
    except subprocess.CalledProcessError as e:
        logger.error('Failed to run {}'.format(cmd)+str(e))
        exit(1)
def main(args):
    logger.info("Start to run TRIMMOMATIC module")
    file_type=['fastq','fq']
    if not str(args.read1).endswith(tuple(file_type)) and not str(args.read2).endswith(tuple(file_type)):
        logger.error(f"Accepted file types are {file_type}")
        exit()
    else:
        if args.seqtype == 'PE':
            if args.read1 and args.read2 is not None:
            
                r1_PE= re.sub('.fastq$', '_trimmed_PE.fastq', args.read1)
                r2_PE= re.sub('.fastq$','_trimmed_PE.fastq',args.read2)
                r1_UPE= re.sub('.fastq$', '_trimmed_UPE.fastq', args.read1)
                r2_UPE= re.sub('.fastq$','_trimmed_UPE.fastq',args.read2)
                cmd = f'java -jar Trimmomatic-0.38/trimmomatic-0.38.jar {args.seqtype} -phred33 -trimlog trimming_logs.txt -summary trimming_summary.txt {args.read1} {args.read2} {r1_PE} {r1_UPE} {r2_PE} {r2_UPE} LEADING:15 TRAILING:5 MINLEN:35'
                run_job(cmd)
            else:
                logger.error(f"{args.read1} read1 and {args.read2} read2 are required.")
                exit(1)
        elif args.seqtype == 'SE':
            if args.read1 and args.read2 is not None:
                logger.error(f"{args.read2} read2 is not an accepted when sequencing type is {args.seqtype}")
                exit(1)
            elif args.read1 == None:
                logger.error(f"Please provide {args.read1}")
                exit(1)
            elif args.read1 is not None and args.read2 is None:
                logger.info(f"Trimmomatic {args.seqtype} running!")
                r1_SE = re.sub('.fastq$','_trimmed_SE.fastq',args.read1)
                cmd = f'java -jar Trimmomatic-0.38/trimmomatic-0.38.jar {args.seqtype} -phred33 -trimlog trimming_logs.txt -summary trimming_summary.txt {args.read1} {r1_SE} LEADING:15 TRAILING:5 MINLEN:35'
        #print(cmd)
                run_job(cmd)
        elif args.seqtype == None:
            logger.error("Please provide {args.seqtype}")
            exit(1)
        else:
            logger.error("Invalid sequencing type : {args.seqtype}, accepted values are : PE or SE")
            exit(1)
        logger.info("Done")
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Run Trimmomatic")
    parser.add_argument("-r1","--read1",type=str,required=True, help="forward read")
    parser.add_argument("-r2","--read2",type=str,required=False, help="reverse read")
    parser.add_argument("-seqtype","--seqtype", type=str, help="sequencing type , accepted values : PE or SE", required= True)
    args = parser.parse_args()
    main(args)
    
        
        
        
    