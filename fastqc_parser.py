import os
import subprocess
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s", datefmt="%m-%d-%Y %H:%M:%S %Z")
logger = logging.getLogger(__name__)
VERSION = 'VERSION: 1.0.0'
AUTHOR = 'AUTHOR: Aishwarya Rane, aishwaryrane08@gmail.com, 11/03/2023'

logger.info(VERSION)
logger.info(AUTHOR)
def run_job(cmd):
    try:
        subprocess.check_call(cmd, shell=True)
    except subprocess.CalledProcessError as e:
        logger.error('Failed to run {}'.format(cmd)+str(e))
        exit(1)
def main(args):
    logger.info("Start to run FASTQC module")
    if not args.outdir:
        logger.info(f"Current working directory is used for saving the output files:{os.getcwd()}")
        args.outdir=os.getcwd()
    for i in range(len(args.in_file)):
        file_type =[".fq",".fastq",".bam",".sam"]
        if not str(args.in_file[i]).endswith(tuple(file_type)):
            logger.error(f"File format is not correct. Got {args.in_file[i]}, Exit!")
            exit(1)
        cmd=f'fastqc {args.in_file[i]} -o {args.outdir}'
        run_job(cmd)
    logger.info("Done")
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Run bcftools")
    parser.add_argument("-in_file","--in_file",nargs='+',required=True, help="Input files")
    parser.add_argument("-outdir","--outdir", type=str, help="Output dircteory")
    args = parser.parse_args()
    main(args)
    