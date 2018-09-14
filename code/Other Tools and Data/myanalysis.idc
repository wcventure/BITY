#include <idc.idc>
static main()
{
  
  // turn on coagulation of data in the final pass of analysis
  SetShortPrm(INF_AF2, GetShortPrm(INF_AF2) | AF2_DODATA);

  Message("Waiting for the end of the auto analysis...\n");
  Wait();

  Message("\n\n------ Creating the output file.... --------\n");

  auto file = GetInputFilePath()[0:-4] + ".asm";
  GenerateFile(OFILE_LST,fopen(file,"w"), 0, BADADDR, 0);           // create the assembler file

  Message("All done, exiting...\n");
  Exit(0);                              // exit to OS, error code 0 - success

}