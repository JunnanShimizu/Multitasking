# Junnan Shimizu
# Project 5
# 3/20/22
# CS337


import multitasking_code
import serial_code


if __name__ == '__main__':
    files = ['reddit_comments_2009.txt', 'reddit_comments_2010.txt', 'reddit_comments_2011.txt',
             'reddit_comments_2012.txt', 'reddit_comments_2013.txt', 'reddit_comments_2014.txt',
             'reddit_comments_2015.txt']
    serial_code.read_file(files)
    print('----------MULTITASKING IMPLEMENTED----------')
    multitasking_code.read_files(files)
