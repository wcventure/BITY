package com;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.FilenameFilter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


public class Main {

	protected static void split(String dec, PrintWriter out) {
		//trim();
		int pointer = dec.lastIndexOf('*');
		if(pointer < 0) pointer = dec.lastIndexOf(' ');
		else pointer++;
		out.print(dec.substring(pointer).trim()+'\t' + dec.substring(0, pointer).trim());
	}
	
	protected static void split_arg(String dec, PrintWriter out) {
		//trim();
		Pattern p_dec = Pattern.compile("(.+);\\s*//(.+)"); 
		Matcher m = p_dec.matcher(dec); 
		if(!m.matches()) return;
		split(m.group(1).trim(), out);
		out.print('\t'+m.group(2).trim());
	}
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		FileOutputStream fos = null;
		PrintWriter out = null;
		BufferedReader reader  = null;
		String path = "./IDA/";
		File apkFile = new File(path);
		Pattern p_fun = Pattern.compile("((\\w*\\s+)*)(\\w+)\\((.+)\\)"); 
		
		if (apkFile.isDirectory()) {
			String[] dirFiles = apkFile.list(new FilenameFilter() {
			
				@Override
				public boolean accept(File dir, String name) {
					return (name.endsWith("IDAF5.txt"));
				}
			
			});
			String[] dirFiles_strip = apkFile.list(new FilenameFilter() {
				
				@Override
				public boolean accept(File dir, String name) {
					return (name.endsWith("strip.txt"));
				}
			
			});
			
			String result = "result.txt";
			try {
				fos = new FileOutputStream(result);
				out = new PrintWriter(fos);
				String line = null;
				//String sym,time, max, min, ave, fail;
				int count = 0;
				String funname = null;
				String paras = null;
				String[] paralist = null;
				//String[] pairs = null;
				for (String s : dirFiles) {
					File fis = new File(path + File.separator + s);
					reader = new BufferedReader(new FileReader(fis));				
					
					//the fitst line
					line = reader.readLine();
					Matcher m = p_fun.matcher(line); 
					if(!m.matches()) continue;
					
					funname = m.group(3);
					out.println(funname+'\t'+s);
					paras = m.group(4);
					//System.out.println(paras);
					paralist = paras.split(",");
					for(int i = 0; i < paralist.length; i++) {
						split(paralist[i].trim(), out);
						out.println();		
					}
					
					reader.readLine();//the 2nd line, "{"
					line = reader.readLine().trim();
					while(line.length() > 0) {
						split_arg(line, out);
						out.println();
						line = reader.readLine();
					}
					count++;
					
					/*
					//1_num_100_len_1000_width_30_rs_2-161020-220242
					be = s.indexOf("width")+6;
					en = s.indexOf('_', be);
					out.print(s.substring(be,en));
					out.print('\t');
					
					be = en + 4;
					en = be+1;
					out.print(s.substring(be,en));
					out.print('\t');
					
					
					System.out.println("Analysis Files: "+ s);
					File fis = new File(path + File.separator + s);
					reader = new BufferedReader(new FileReader(fis));
					
					line = reader.readLine();
					out.print(line.substring(line.lastIndexOf(' ')+1));
					
					while((line = reader.readLine())!=null) {
						out.print('\t');
						out.print(line.substring(line.indexOf(':')+2));
					}
					out.println();
					reader.close();
					count++;*/
				}
				System.out.println("Total Files: "+count);
					
				out.close();
				fos.close();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
				System.out.println(e.getMessage());
			}
			
		} 
		else {
			System.out.println("not a directory!");
		}
	}

}
