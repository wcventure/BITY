;
; +-------------------------------------------------------------------------+
; |   This file	has been generated by The Interactive Disassembler (IDA)    |
; |	      Copyright	(c) 2015 Hex-Rays, <support@hex-rays.com>	    |
; |			 License info: 48-B611-7234-BB			    |
; |		Doskey Lee, Kingsoft Internet Security Software		    |
; +-------------------------------------------------------------------------+
;
; Input	MD5   :	14EDEFA1C745CACDB89871F73F453395
; Input	CRC32 :	3B6DD461

; File Name   :	D:\coreutils-o\rmdir.o
; Format      :	ELF for	Intel 386 (Relocatable)
;
; Source File :	'rmdir.c'

		.686p
		.mmx
		.model flat
.intel_syntax noprefix

; ===========================================================================

; Segment type:	Pure code
; Segment permissions: Read/Execute
_text		segment	byte public 'CODE' use32
		assume cs:_text
		;org 8000000h
		assume es:nothing, ss:nothing, ds:_text, fs:nothing, gs:nothing

; =============== S U B	R O U T	I N E =======================================

; Attributes: static bp-based frame

; _Bool	__cdecl	dot_or_dotdot(const char *file_name)
dot_or_dotdot	proc near		; CODE XREF: readdir_ignoring_dot_and_dotdot+27p

sep		= byte ptr -1
file_name	= dword	ptr  8

		push	ebp
		mov	ebp, esp
		sub	esp, 10h
		mov	eax, [ebp+file_name]
		movzx	eax, byte ptr [eax]
		cmp	al, 2Eh
		jnz	short loc_8000051
		mov	eax, [ebp+file_name]
		add	eax, 1
		movzx	eax, byte ptr [eax]
		cmp	al, 2Eh
		jnz	short loc_8000024
		mov	edx, 2
		jmp	short loc_8000029
; ---------------------------------------------------------------------------

loc_8000024:				; CODE XREF: dot_or_dotdot+1Bj
		mov	edx, 1

loc_8000029:				; CODE XREF: dot_or_dotdot+22j
		mov	eax, [ebp+file_name]
		add	eax, edx
		movzx	eax, byte ptr [eax]
		mov	[ebp+sep], al
		cmp	[ebp+sep], 0
		jz	short loc_8000040
		cmp	[ebp+sep], 2Fh
		jnz	short loc_8000047

loc_8000040:				; CODE XREF: dot_or_dotdot+38j
		mov	eax, 1
		jmp	short loc_800004C
; ---------------------------------------------------------------------------

loc_8000047:				; CODE XREF: dot_or_dotdot+3Ej
		mov	eax, 0

loc_800004C:				; CODE XREF: dot_or_dotdot+45j
		and	eax, 1
		jmp	short locret_8000056
; ---------------------------------------------------------------------------

loc_8000051:				; CODE XREF: dot_or_dotdot+Ej
		mov	eax, 0

locret_8000056:				; CODE XREF: dot_or_dotdot+4Fj
		leave
		retn
dot_or_dotdot	endp


; =============== S U B	R O U T	I N E =======================================

; Attributes: static bp-based frame

; const	dirent *__cdecl	readdir_ignoring_dot_and_dotdot(DIR *dirp)
readdir_ignoring_dot_and_dotdot	proc near ; CODE XREF: is_empty_dir+69p

dp		= dword	ptr -0Ch
dirp		= dword	ptr  8

		push	ebp
		mov	ebp, esp
		sub	esp, 18h

loc_800005E:				; CODE XREF: readdir_ignoring_dot_and_dotdot+34j
		sub	esp, 0Ch
		push	[ebp+dirp]
		call	readdir64
		add	esp, 10h
		mov	[ebp+dp], eax
		cmp	[ebp+dp], 0
		jz	short loc_800008E
		mov	eax, [ebp+dp]
		add	eax, 13h
		sub	esp, 0Ch
		push	eax		; file_name
		call	dot_or_dotdot
		add	esp, 10h
		xor	eax, 1
		test	al, al
		jz	short loc_800005E

loc_800008E:				; CODE XREF: readdir_ignoring_dot_and_dotdot+1Bj
		mov	eax, [ebp+dp]
		leave
		retn
readdir_ignoring_dot_and_dotdot	endp


; =============== S U B	R O U T	I N E =======================================

; Attributes: static bp-based frame

; _Bool	__cdecl	is_empty_dir(int fd_cwd, const char *dir)
is_empty_dir	proc near		; CODE XREF: ignorable_failure+37p

fd		= dword	ptr -18h
dirp		= dword	ptr -14h
dp		= dword	ptr -10h
saved_errno	= dword	ptr -0Ch
fd_cwd		= dword	ptr  8
dir		= dword	ptr  0Ch

		push	ebp
		mov	ebp, esp
		sub	esp, 18h
		sub	esp, 4
		push	30900h
		push	[ebp+dir]
		push	[ebp+fd_cwd]
		call	openat64
		add	esp, 10h
		mov	[ebp+fd], eax
		cmp	[ebp+fd], 0
		jns	short loc_80000BF
		mov	eax, 0
		jmp	short locret_8000133
; ---------------------------------------------------------------------------

loc_80000BF:				; CODE XREF: is_empty_dir+23j
		sub	esp, 0Ch
		push	[ebp+fd]
		call	fdopendir
		add	esp, 10h
		mov	[ebp+dirp], eax
		cmp	[ebp+dirp], 0
		jnz	short loc_80000EB
		sub	esp, 0Ch
		push	[ebp+fd]	; fd
		call	close
		add	esp, 10h
		mov	eax, 0
		jmp	short locret_8000133
; ---------------------------------------------------------------------------

loc_80000EB:				; CODE XREF: is_empty_dir+41j
		call	__errno_location
		mov	dword ptr [eax], 0
		sub	esp, 0Ch
		push	[ebp+dirp]	; dirp
		call	readdir_ignoring_dot_and_dotdot
		add	esp, 10h
		mov	[ebp+dp], eax
		call	__errno_location
		mov	eax, [eax]
		mov	[ebp+saved_errno], eax
		sub	esp, 0Ch
		push	[ebp+dirp]	; dirp
		call	closedir
		add	esp, 10h
		cmp	[ebp+dp], 0
		jz	short loc_800012C
		mov	eax, 0
		jmp	short locret_8000133
; ---------------------------------------------------------------------------

loc_800012C:				; CODE XREF: is_empty_dir+90j
		cmp	[ebp+saved_errno], 0
		setz	al

locret_8000133:				; CODE XREF: is_empty_dir+2Aj
					; is_empty_dir+56j ...
		leave
		retn
is_empty_dir	endp


; =============== S U B	R O U T	I N E =======================================

; Attributes: static bp-based frame

; void emit_ancillary_info()
emit_ancillary_info proc near		; CODE XREF: usage+ECp

lc_messages	= dword	ptr -0Ch
var_4		= dword	ptr -4

		push	ebp
		mov	ebp, esp
		push	ebx
		sub	esp, 14h
		mov	eax, ds:program_name
		sub	esp, 0Ch
		push	eax
		call	last_component
		add	esp, 10h
		mov	ebx, eax
		sub	esp, 0Ch
		push	offset msgid	; "\nReport %s bugs to %s\n"
		call	gettext
		add	esp, 10h
		sub	esp, 4
		push	offset aBugCoreutils@g ; "bug-coreutils@gnu.org"
		push	ebx
		push	eax		; format
		call	printf
		add	esp, 10h
		sub	esp, 0Ch
		push	offset aSHomePageHttpW ; "%s home page:	<http://www.gnu.org/softw"...
		call	gettext
		add	esp, 10h
		sub	esp, 4
		push	offset domainname ; "coreutils"
		push	offset aGnuCoreutils ; "GNU coreutils"
		push	eax		; format
		call	printf
		add	esp, 10h
		mov	ebx, ds:stdout
		sub	esp, 0Ch
		push	offset aGeneralHelpUsi ; "General help using GNU software: <http:"...
		call	gettext
		add	esp, 10h
		sub	esp, 8
		push	ebx
		push	eax
		call	fputs_unlocked
		add	esp, 10h
		sub	esp, 8
		push	0		; locale
		push	5		; category
		call	setlocale
		add	esp, 10h
		mov	[ebp+lc_messages], eax
		cmp	[ebp+lc_messages], 0
		jz	short loc_800021B
		sub	esp, 4
		push	3		; n
		push	offset s2	; "en_"
		push	[ebp+lc_messages] ; s1
		call	strncmp
		add	esp, 10h
		test	eax, eax
		jz	short loc_800021B
		mov	eax, ds:program_name
		sub	esp, 0Ch
		push	eax
		call	last_component
		add	esp, 10h
		mov	ebx, eax
		sub	esp, 0Ch
		push	offset aReportSTransla ; "Report %s translation	bugs to	<http://t"...
		call	gettext
		add	esp, 10h
		sub	esp, 8
		push	ebx
		push	eax		; format
		call	printf
		add	esp, 10h

loc_800021B:				; CODE XREF: emit_ancillary_info+9Bj
					; emit_ancillary_info+B4j
		mov	eax, ds:program_name
		sub	esp, 0Ch
		push	eax
		call	last_component
		add	esp, 10h
		mov	ebx, eax
		sub	esp, 0Ch
		push	offset aForCompleteDoc ; "For complete documentation, run: info	c"...
		call	gettext
		add	esp, 10h
		sub	esp, 8
		push	ebx
		push	eax		; format
		call	printf
		add	esp, 10h
		nop
		mov	ebx, [ebp+var_4]
		leave
		retn
emit_ancillary_info endp


; =============== S U B	R O U T	I N E =======================================

; Attributes: static bp-based frame

; _Bool	__cdecl	errno_rmdir_non_empty(int error_number)
errno_rmdir_non_empty proc near		; CODE XREF: ignorable_failure+14p

error_number	= dword	ptr  8

		push	ebp
		mov	ebp, esp
		cmp	[ebp+error_number], 27h
		jz	short loc_8000260
		cmp	[ebp+error_number], 11h
		jnz	short loc_8000267

loc_8000260:				; CODE XREF: errno_rmdir_non_empty+7j
		mov	eax, 1
		jmp	short loc_800026C
; ---------------------------------------------------------------------------

loc_8000267:				; CODE XREF: errno_rmdir_non_empty+Dj
		mov	eax, 0

loc_800026C:				; CODE XREF: errno_rmdir_non_empty+14j
		and	eax, 1
		pop	ebp
		retn
errno_rmdir_non_empty endp


; =============== S U B	R O U T	I N E =======================================

; Attributes: static bp-based frame

; _Bool	__cdecl	errno_may_be_empty(int error_number)
errno_may_be_empty proc	near		; CODE XREF: ignorable_failure+23p

error_number	= dword	ptr  8

		push	ebp
		mov	ebp, esp
		cmp	[ebp+error_number], 1Eh	; switch 31 cases
		ja	short loc_8000290 ; jumptable 08000287 default case
		mov	eax, [ebp+error_number]
		shl	eax, 2
		add	eax, offset off_80009B0
		mov	eax, [eax]
		jmp	eax		; switch jump
; ---------------------------------------------------------------------------

loc_8000289:				; CODE XREF: errno_may_be_empty+16j
					; DATA XREF: .rodata:off_80009B0o
		mov	eax, 1		; jumptable 08000287 cases 1,13,16,17,30
		jmp	short loc_8000295
; ---------------------------------------------------------------------------

loc_8000290:				; CODE XREF: errno_may_be_empty+7j
					; errno_may_be_empty+16j
					; DATA XREF: ...
		mov	eax, 0		; jumptable 08000287 default case

loc_8000295:				; CODE XREF: errno_may_be_empty+1Dj
		pop	ebp
		retn
errno_may_be_empty endp


; =============== S U B	R O U T	I N E =======================================

; Attributes: static bp-based frame

; _Bool	__cdecl	ignorable_failure(int error_number, const char *dir)
ignorable_failure proc near		; CODE XREF: remove_parents+CBp
					; main+1E1p

error_number	= dword	ptr  8
dir		= dword	ptr  0Ch

		push	ebp
		mov	ebp, esp
		sub	esp, 8
		movzx	eax, ds:ignore_fail_on_non_empty
		test	al, al
		jz	short loc_80002E1
		push	[ebp+error_number] ; error_number
		call	errno_rmdir_non_empty
		add	esp, 4
		test	al, al
		jnz	short loc_80002DA
		push	[ebp+error_number] ; error_number
		call	errno_may_be_empty
		add	esp, 4
		test	al, al
		jz	short loc_80002E1
		sub	esp, 8
		push	[ebp+dir]	; dir
		push	0FFFFFF9Ch	; fd_cwd
		call	is_empty_dir
		add	esp, 10h
		test	al, al
		jz	short loc_80002E1

loc_80002DA:				; CODE XREF: ignorable_failure+1Ej
		mov	eax, 1
		jmp	short loc_80002E6
; ---------------------------------------------------------------------------

loc_80002E1:				; CODE XREF: ignorable_failure+Fj
					; ignorable_failure+2Dj ...
		mov	eax, 0

loc_80002E6:				; CODE XREF: ignorable_failure+48j
		and	eax, 1
		leave
		retn
ignorable_failure endp


; =============== S U B	R O U T	I N E =======================================

; Attributes: static bp-based frame

; _Bool	__cdecl	remove_parents(char *dir)
remove_parents	proc near		; CODE XREF: main+23Ap

ok		= byte ptr -0Dh
slash		= dword	ptr -0Ch
dir		= dword	ptr  8

		push	ebp
		mov	ebp, esp
		push	esi
		push	ebx
		sub	esp, 10h
		mov	[ebp+ok], 1
		sub	esp, 0Ch
		push	[ebp+dir]
		call	strip_trailing_slashes
		add	esp, 10h

loc_8000305:				; CODE XREF: remove_parents+B7j
		sub	esp, 8
		push	2Fh		; c
		push	[ebp+dir]	; s
		call	strrchr
		add	esp, 10h
		mov	[ebp+slash], eax
		cmp	[ebp+slash], 0
		jz	loc_8000400
		jmp	short loc_8000328
; ---------------------------------------------------------------------------

loc_8000324:				; CODE XREF: remove_parents+4Dj
		sub	[ebp+slash], 1

loc_8000328:				; CODE XREF: remove_parents+37j
		mov	eax, [ebp+slash]
		cmp	eax, [ebp+dir]
		jbe	short loc_800033A
		mov	eax, [ebp+slash]
		movzx	eax, byte ptr [eax]
		cmp	al, 2Fh
		jz	short loc_8000324

loc_800033A:				; CODE XREF: remove_parents+43j
		mov	eax, [ebp+slash]
		add	eax, 1
		mov	byte ptr [eax],	0
		movzx	eax, ds:verbose
		test	al, al
		jz	short loc_8000383
		sub	esp, 0Ch
		push	[ebp+dir]
		call	quote
		add	esp, 10h
		mov	ebx, eax
		sub	esp, 0Ch
		push	offset aRemovingDirect ; "removing directory, %s"
		call	gettext
		add	esp, 10h
		mov	edx, eax
		mov	eax, ds:stdout
		sub	esp, 4
		push	ebx
		push	edx
		push	eax
		call	prog_fprintf
		add	esp, 10h

loc_8000383:				; CODE XREF: remove_parents+61j
		sub	esp, 0Ch
		push	[ebp+dir]	; path
		call	rmdir
		add	esp, 10h
		test	eax, eax
		setz	al
		mov	[ebp+ok], al
		movzx	eax, [ebp+ok]
		xor	eax, 1
		test	al, al
		jz	loc_8000305
		call	__errno_location
		mov	eax, [eax]
		sub	esp, 8
		push	[ebp+dir]	; dir
		push	eax		; error_number
		call	ignorable_failure
		add	esp, 10h
		test	al, al
		jz	short loc_80003C8
		mov	[ebp+ok], 1
		jmp	short loc_8000401
; ---------------------------------------------------------------------------

loc_80003C8:				; CODE XREF: remove_parents+D5j
		sub	esp, 0Ch
		push	[ebp+dir]
		call	quote
		add	esp, 10h
		mov	esi, eax
		sub	esp, 0Ch
		push	offset aFailedToRemove ; "failed to remove directory %s"
		call	gettext
		add	esp, 10h
		mov	ebx, eax
		call	__errno_location
		mov	eax, [eax]
		push	esi
		push	ebx		; format
		push	eax		; errnum
		push	0		; status
		call	error
		add	esp, 10h
		jmp	short loc_8000401
; ---------------------------------------------------------------------------

loc_8000400:				; CODE XREF: remove_parents+31j
		nop

loc_8000401:				; CODE XREF: remove_parents+DBj
					; remove_parents+113j
		movzx	eax, [ebp+ok]
		lea	esp, [ebp-8]
		pop	ebx
		pop	esi
		pop	ebp
		retn
remove_parents	endp


; =============== S U B	R O U T	I N E =======================================

; Attributes: noreturn bp-based	frame

; void __cdecl usage(int status)
		public usage
usage		proc near		; CODE XREF: main+C9p main+106p ...

status		= dword	ptr  8

		push	ebp
		mov	ebp, esp
		push	ebx
		sub	esp, 4
		cmp	[ebp+status], 0
		jz	short loc_8000449
		mov	ebx, ds:program_name
		sub	esp, 0Ch
		push	offset aTrySHelpForMor ; "Try `%s --help' for more information.\n"
		call	gettext
		add	esp, 10h
		mov	edx, eax
		mov	eax, ds:stderr
		sub	esp, 4
		push	ebx
		push	edx		; format
		push	eax		; stream
		call	fprintf
		add	esp, 10h
		jmp	loc_80004FD
; ---------------------------------------------------------------------------

loc_8000449:				; CODE XREF: usage+Bj
		mov	ebx, ds:program_name
		sub	esp, 0Ch
		push	offset aUsageSOption__ ; "Usage: %s [OPTION]...	DIRECTORY...\n"
		call	gettext
		add	esp, 10h
		sub	esp, 8
		push	ebx
		push	eax		; format
		call	printf
		add	esp, 10h
		mov	ebx, ds:stdout
		sub	esp, 0Ch
		push	offset aRemoveTheDirec ; "Remove the DIRECTORY(ies), if	they are "...
		call	gettext
		add	esp, 10h
		sub	esp, 8
		push	ebx
		push	eax
		call	fputs_unlocked
		add	esp, 10h
		mov	ebx, ds:stdout
		sub	esp, 0Ch
		push	offset aPParentsRemove ; "  -p,	--parents   remove DIRECTORY and "...
		call	gettext
		add	esp, 10h
		sub	esp, 8
		push	ebx
		push	eax
		call	fputs_unlocked
		add	esp, 10h
		mov	ebx, ds:stdout
		sub	esp, 0Ch
		push	offset aHelpDisplayThi ; "	--help	   display this	help and "...
		call	gettext
		add	esp, 10h
		sub	esp, 8
		push	ebx
		push	eax
		call	fputs_unlocked
		add	esp, 10h
		mov	ebx, ds:stdout
		sub	esp, 0Ch
		push	offset aVersionOutputV ; "	--version  output version informa"...
		call	gettext
		add	esp, 10h
		sub	esp, 8
		push	ebx
		push	eax
		call	fputs_unlocked
		add	esp, 10h
		call	emit_ancillary_info

loc_80004FD:				; CODE XREF: usage+38j
		sub	esp, 0Ch
		push	[ebp+status]	; status
		call	exit
usage		endp


; =============== S U B	R O U T	I N E =======================================

; Attributes: noreturn bp-based	frame

; int __cdecl main(int argc, const char	**argv,	const char **envp)
		public main
main		proc near

ok		= byte ptr -21h
optc		= dword	ptr -20h
dir		= dword	ptr -1Ch
argc		= dword	ptr  0Ch
argv		= dword	ptr  10h
envp		= dword	ptr  14h

		lea	ecx, [esp+4]
		and	esp, 0FFFFFFF0h
		push	dword ptr [ecx-4]
		push	ebp
		mov	ebp, esp
		push	edi
		push	esi
		push	ebx
		push	ecx
		sub	esp, 18h
		mov	ebx, ecx
		mov	[ebp+ok], 1
		mov	eax, [ebx+4]
		mov	eax, [eax]
		sub	esp, 0Ch
		push	eax
		call	set_program_name
		add	esp, 10h
		sub	esp, 8
		push	offset locale	; locale
		push	6		; category
		call	setlocale
		add	esp, 10h
		sub	esp, 8
		push	offset dirname	; "/usr/local/share/locale"
		push	offset domainname ; "coreutils"
		call	bindtextdomain
		add	esp, 10h
		sub	esp, 0Ch
		push	offset domainname ; "coreutils"
		call	textdomain
		add	esp, 10h
		sub	esp, 0Ch
		push	offset close_stdout ; func
		call	atexit
		add	esp, 10h
		mov	ds:remove_empty_parents, 0
		jmp	loc_8000613
; ---------------------------------------------------------------------------

loc_8000586:				; CODE XREF: main+12Ej
		mov	eax, [ebp+optc]
		cmp	eax, 70h
		jz	short loc_80005B1
		cmp	eax, 70h
		jg	short loc_80005A3
		cmp	eax, 0FFFFFF7Dh
		jz	short loc_80005D6
		cmp	eax, 0FFFFFF7Eh
		jz	short loc_80005CC
		jmp	short loc_8000609
; ---------------------------------------------------------------------------

loc_80005A3:				; CODE XREF: main+89j
		cmp	eax, 76h
		jz	short loc_80005C3
		cmp	eax, 80h
		jz	short loc_80005BA
		jmp	short loc_8000609
; ---------------------------------------------------------------------------

loc_80005B1:				; CODE XREF: main+84j
		mov	ds:remove_empty_parents, 1
		jmp	short loc_8000613
; ---------------------------------------------------------------------------

loc_80005BA:				; CODE XREF: main+A5j
		mov	ds:ignore_fail_on_non_empty, 1
		jmp	short loc_8000613
; ---------------------------------------------------------------------------

loc_80005C3:				; CODE XREF: main+9Ej
		mov	ds:verbose, 1
		jmp	short loc_8000613
; ---------------------------------------------------------------------------

loc_80005CC:				; CODE XREF: main+97j
		sub	esp, 0Ch
		push	0		; status
		call	usage
; ---------------------------------------------------------------------------

loc_80005D6:				; CODE XREF: main+90j
		mov	edx, ds:Version
		mov	eax, ds:stdout
		sub	esp, 8
		push	0
		push	offset aDavidMackenzie ; "David	MacKenzie"
		push	edx
		push	offset aGnuCoreutils ; "GNU coreutils"
		push	offset aRmdir	; "rmdir"
		push	eax
		call	version_etc
		add	esp, 20h
		sub	esp, 0Ch
		push	0		; status
		call	exit
; ---------------------------------------------------------------------------

loc_8000609:				; CODE XREF: main+99j main+A7j
		sub	esp, 0Ch
		push	1		; status
		call	usage
; ---------------------------------------------------------------------------

loc_8000613:				; CODE XREF: main+79j main+B0j ...
		sub	esp, 0Ch
		push	0		; longind
		push	offset longopts	; longopts
		push	offset shortopts ; "pv"
		push	dword ptr [ebx+4] ; argv
		push	dword ptr [ebx]	; argc
		call	getopt_long
		add	esp, 20h
		mov	[ebp+optc], eax
		cmp	[ebp+optc], 0FFFFFFFFh
		jnz	loc_8000586
		mov	eax, ds:optind
		cmp	eax, [ebx]
		jnz	loc_800076B
		sub	esp, 0Ch
		push	offset aMissingOperand ; "missing operand"
		call	gettext
		add	esp, 10h
		sub	esp, 4
		push	eax		; format
		push	0		; errnum
		push	0		; status
		call	error
		add	esp, 10h
		sub	esp, 0Ch
		push	1		; status
		call	usage
; ---------------------------------------------------------------------------

loc_8000673:				; CODE XREF: main+26Aj
		mov	eax, ds:optind
		lea	edx, ds:0[eax*4]
		mov	eax, [ebx+4]
		add	eax, edx
		mov	eax, [eax]
		mov	[ebp+dir], eax
		movzx	eax, ds:verbose
		test	al, al
		jz	short loc_80006C9
		sub	esp, 0Ch
		push	[ebp+dir]
		call	quote
		add	esp, 10h
		mov	esi, eax
		sub	esp, 0Ch
		push	offset aRemovingDirect ; "removing directory, %s"
		call	gettext
		add	esp, 10h
		mov	edx, eax
		mov	eax, ds:stdout
		sub	esp, 4
		push	esi
		push	edx
		push	eax
		call	prog_fprintf
		add	esp, 10h

loc_80006C9:				; CODE XREF: main+18Aj
		sub	esp, 0Ch
		push	[ebp+dir]	; path
		call	rmdir
		add	esp, 10h
		test	eax, eax
		jz	short loc_8000731
		call	__errno_location
		mov	eax, [eax]
		sub	esp, 8
		push	[ebp+dir]	; dir
		push	eax		; error_number
		call	ignorable_failure
		add	esp, 10h
		test	al, al
		jnz	short loc_800075D
		sub	esp, 0Ch
		push	[ebp+dir]
		call	quote
		add	esp, 10h
		mov	edi, eax
		sub	esp, 0Ch
		push	offset aFailedToRemo_0 ; "failed to remove %s"
		call	gettext
		add	esp, 10h
		mov	esi, eax
		call	__errno_location
		mov	eax, [eax]
		push	edi
		push	esi		; format
		push	eax		; errnum
		push	0		; status
		call	error
		add	esp, 10h
		mov	[ebp+ok], 0
		jmp	short loc_800075E
; ---------------------------------------------------------------------------

loc_8000731:				; CODE XREF: main+1D1j
		movzx	eax, ds:remove_empty_parents
		test	al, al
		jz	short loc_800075E
		sub	esp, 0Ch
		push	[ebp+dir]	; dir
		call	remove_parents
		add	esp, 10h
		movzx	edx, [ebp+ok]
		movzx	eax, al
		and	eax, edx
		test	eax, eax
		setnz	al
		mov	[ebp+ok], al
		jmp	short loc_800075E
; ---------------------------------------------------------------------------

loc_800075D:				; CODE XREF: main+1EBj
		nop

loc_800075E:				; CODE XREF: main+227j	main+232j ...
		mov	eax, ds:optind
		add	eax, 1
		mov	ds:optind, eax

loc_800076B:				; CODE XREF: main+13Bj
		mov	eax, ds:optind
		cmp	eax, [ebx]
		jl	loc_8000673
		cmp	[ebp+ok], 0
		jz	short loc_8000785
		mov	eax, 0
		jmp	short loc_800078A
; ---------------------------------------------------------------------------

loc_8000785:				; CODE XREF: main+274j
		mov	eax, 1

loc_800078A:				; CODE XREF: main+27Bj
		sub	esp, 0Ch
		push	eax		; status

loc_800078E:				; DATA XREF: .eh_frame:08000D10o
					; .eh_frame:08000D30o ...
		call	exit
main		endp

_text		ends

; ===========================================================================

; Segment type:	Zero-length
; Segment permissions: Read/Write
_data		segment	byte public 'DATA' use32
_data		ends

; ===========================================================================

; Segment type:	Uninitialized
; Segment permissions: Read/Write
_bss		segment	byte public 'BSS' use32
		assume cs:_bss
		;org 8000794h
		assume es:nothing, ss:nothing, ds:_text, fs:nothing, gs:nothing
; _Bool	remove_empty_parents
remove_empty_parents db	?		; DATA XREF: main+72w
					; main:loc_80005B1w ...
; _Bool	ignore_fail_on_non_empty
ignore_fail_on_non_empty db ?		; DATA XREF: ignorable_failure+6r
					; main:loc_80005BAw
; _Bool	verbose
verbose		db ?			; DATA XREF: remove_parents+58r
					; main:loc_80005C3w ...
_bss		ends

; ===========================================================================

; Segment type:	Pure data
; Segment permissions: Read
; Segment alignment '32byte' can not be represented in assembly
_rodata		segment	para public 'CONST' use32
		assume cs:_rodata
		;org 80007A0h
; char msgid[]
msgid		db 0Ah			; DATA XREF: emit_ancillary_info+1Do
		db 'Report %s bugs to %s',0Ah,0
aBugCoreutils@g	db 'bug-coreutils@gnu.org',0 ; DATA XREF: emit_ancillary_info+2Do
		align 10h
; char aSHomePageHttpW[]
aSHomePageHttpW	db '%s home page: <http://www.gnu.org/software/%s/>',0Ah,0
					; DATA XREF: emit_ancillary_info+3Fo
; char domainname[]
domainname	db 'coreutils',0        ; DATA XREF: emit_ancillary_info+4Fo
					; main+45o ...
aGnuCoreutils	db 'GNU coreutils',0    ; DATA XREF: emit_ancillary_info+54o
					; main+E4o
		align 4
; char aGeneralHelpUsi[]
aGeneralHelpUsi	db 'General help using GNU software: <http://www.gnu.org/gethelp/>',0Ah,0
					; DATA XREF: emit_ancillary_info+6Bo
; char s2[]
s2		db 'en_',0              ; DATA XREF: emit_ancillary_info+A2o
; char aReportSTransla[]
aReportSTransla	db 'Report %s translation bugs to <http://translationproject.org/team'
					; DATA XREF: emit_ancillary_info+CCo
		db '/>',0Ah,0
		align 4
; char aForCompleteDoc[]
aForCompleteDoc	db 'For complete documentation, run: info coreutils ',27h,'%s invocation'
					; DATA XREF: emit_ancillary_info+FCo
		db 27h,0Ah,0
aIgnoreFailOnNo	db 'ignore-fail-on-non-empty',0 ; DATA XREF: .rodata:longoptso
aPath		db 'path',0             ; DATA XREF: .rodata:longoptso
aParents	db 'parents',0          ; DATA XREF: .rodata:longoptso
aVerbose	db 'verbose',0          ; DATA XREF: .rodata:longoptso
aHelp		db 'help',0             ; DATA XREF: .rodata:longoptso
aVersion	db 'version',0          ; DATA XREF: .rodata:longoptso
		align 20h
; const	option longopts[7]
longopts	option <offset aIgnoreFailOnNo,	0, 0, 80h> ; DATA XREF:	main+110o
		option <offset aPath, 0, 0, 70h> ; "ignore-fail-on-non-empty"
		option <offset aParents, 0, 0, 70h>
		option <offset aVerbose, 0, 0, 76h>
		option <offset aHelp, 0, 0, 0FFFFFF7Eh>
		option <offset aVersion, 0, 0, 0FFFFFF7Dh>
		option	<0>
off_80009B0	dd offset loc_8000290	; DATA XREF: errno_may_be_empty+Fo
		dd offset loc_8000289	; jump table for switch	statement
		dd offset loc_8000290
		dd offset loc_8000290
		dd offset loc_8000290
		dd offset loc_8000290
		dd offset loc_8000290
		dd offset loc_8000290
		dd offset loc_8000290
		dd offset loc_8000290
		dd offset loc_8000290
		dd offset loc_8000290
		dd offset loc_8000290
		dd offset loc_8000289
		dd offset loc_8000290
		dd offset loc_8000290
		dd offset loc_8000289
		dd offset loc_8000289
		dd offset loc_8000290
		dd offset loc_8000290
		dd offset loc_8000290
		dd offset loc_8000290
		dd offset loc_8000290
		dd offset loc_8000290
		dd offset loc_8000290
		dd offset loc_8000290
		dd offset loc_8000290
		dd offset loc_8000290
		dd offset loc_8000290
		dd offset loc_8000290
		dd offset loc_8000289
; char aRemovingDirect[]
aRemovingDirect	db 'removing directory, %s',0 ; DATA XREF: remove_parents+76o
					; main+19Fo
; char aFailedToRemove[]
aFailedToRemove	db 'failed to remove directory %s',0 ; DATA XREF: remove_parents+F0o
		align 4
; char aTrySHelpForMor[]
aTrySHelpForMor	db 'Try `%s --help',27h,' for more information.',0Ah,0
					; DATA XREF: usage+16o
		align 4
; char aUsageSOption__[]
aUsageSOption__	db 'Usage: %s [OPTION]... DIRECTORY...',0Ah,0 ; DATA XREF: usage+46o
; char aRemoveTheDirec[]
aRemoveTheDirec	db 'Remove the DIRECTORY(ies), if they are empty.',0Ah
					; DATA XREF: usage+69o
		db 0Ah
		db '      --ignore-fail-on-non-empty',0Ah
		db '                  ignore each failure that is solely because a di'
		db 'rectory',0Ah
		db '                    is non-empty',0Ah,0
		align 4
; char aPParentsRemove[]
aPParentsRemove	db '  -p, --parents   remove DIRECTORY and its ancestors; e.g., `rmdi'
					; DATA XREF: usage+8Co
		db 'r -p a/b/c',27h,' is',0Ah
		db '                    similar to `rmdir a/b/c a/b a',27h,0Ah
		db '  -v, --verbose   output a diagnostic for every directory process'
		db 'ed',0Ah,0
; char aHelpDisplayThi[]
aHelpDisplayThi	db '      --help     display this help and exit',0Ah,0
					; DATA XREF: usage+AFo
		align 4
; char aVersionOutputV[]
aVersionOutputV	db '      --version  output version information and exit',0Ah,0
					; DATA XREF: usage+D2o
; char locale
locale		db 0			; DATA XREF: main+2Eo
; char dirname[]
dirname		db '/usr/local/share/locale',0 ; DATA XREF: main+40o
aDavidMackenzie	db 'David MacKenzie',0  ; DATA XREF: main+DEo
aRmdir		db 'rmdir',0            ; DATA XREF: main+E9o
; char shortopts[]
shortopts	db 'pv',0               ; DATA XREF: main+115o
; char aMissingOperand[]
aMissingOperand	db 'missing operand',0  ; DATA XREF: main+144o
; char aFailedToRemo_0[]
aFailedToRemo_0	db 'failed to remove %s',0 ; DATA XREF: main+200o
_rodata		ends

; ===========================================================================

; Segment type:	Pure data
; Segment permissions: Read
_eh_frame	segment	dword public 'CONST' use32
		assume cs:_eh_frame
		;org 8000CF0h
		dd 14h,	0
		dd 527A01h, 1087C01h, 4040C1Bh,	188h, 2	dup(1Ch)
		dd offset loc_800078E-800149Eh
		dd 58h,	80E4100h, 0D420285h, 0C5540205h, 4040Ch, 1Ch, 3Ch
		dd offset loc_800078E-8001466h
		dd 3Bh,	80E4100h, 0D420285h, 0CC57705h,	404h, 1Ch, 5Ch
		dd offset loc_800078E-800144Bh
		dd 0A2h, 80E4100h, 0D420285h, 0C59E0205h, 4040Ch, 20h
		dd 7Ch
		dd offset loc_800078E-80013C9h
		dd 11Ch, 80E4100h, 0D420285h, 3834405h,	0C5011403h, 4040CC3h
		dd 1Ch,	0A0h
		dd offset loc_800078E-80012D1h
		dd 20h,	80E4100h, 0D420285h, 0CC55C05h,	404h, 1Ch, 0C0h
		dd offset loc_800078E-80012D1h
		dd 26h,	80E4100h, 0D420285h, 0CC56205h,	404h, 1Ch, 0E0h
		dd offset loc_800078E-80012CBh
		dd 54h,	80E4100h, 0D420285h, 0C5500205h, 4040Ch, 28h, 100h
		dd offset loc_800078E-8001297h
		dd 121h, 80E4100h, 0D420285h, 3864505h,	16030483h, 0C641C301h
		dd 40CC541h, 4,	18h, 12Ch
		dd offset loc_800078E-80011A2h
		dd 0FCh, 80E4100h, 0D420285h, 3834405h,	2Ch, 148h
		dd offset loc_800078E-80010C2h
		dd 28Bh, 10C4400h, 5104700h, 46007502h,	7075030Fh, 2071006h
		dd 6107C75h, 10787502h,	74750203h
_eh_frame	ends

; ===========================================================================

; Segment type:	Externs
; extern
		extrn readdir64:near	; CODE XREF: readdir_ignoring_dot_and_dotdot+Cp
		extrn openat64:near	; CODE XREF: is_empty_dir+14p
		extrn fdopendir:near	; CODE XREF: is_empty_dir+32p
; int close(int	fd)
		extrn close:near	; CODE XREF: is_empty_dir+49p
; int *_errno_location(void)
		extrn __errno_location:near ; CODE XREF: is_empty_dir:loc_80000EBp
					; is_empty_dir+74p ...
; int closedir(DIR *dirp)
		extrn closedir:near	; CODE XREF: is_empty_dir+84p
		extrn program_name:dword ; DATA	XREF: emit_ancillary_info+7r
					; emit_ancillary_info+B6r ...
		extrn last_component:near ; CODE XREF: emit_ancillary_info+10p
					; emit_ancillary_info+BFp ...
; char *gettext(const char *msgid)
		extrn gettext:near	; CODE XREF: emit_ancillary_info+22p
					; emit_ancillary_info+44p ...
; int printf(const char	*format, ...)
		extrn printf:near	; CODE XREF: emit_ancillary_info+34p
					; emit_ancillary_info+5Ap ...
; struct _IO_FILE *stdout
		extrn stdout:dword	; DATA XREF: emit_ancillary_info+62r
					; remove_parents+85r ...
		extrn fputs_unlocked:near ; CODE XREF: emit_ancillary_info+7Dp
					; usage+7Bp ...
; char *setlocale(int category,	const char *locale)
		extrn setlocale:near	; CODE XREF: emit_ancillary_info+8Cp
					; main+35p
; int strncmp(const char *s1, const char *s2, size_t n)
		extrn strncmp:near	; CODE XREF: emit_ancillary_info+AAp
		extrn strip_trailing_slashes:near ; CODE XREF: remove_parents+12p
; char *strrchr(const char *s, int c)
		extrn strrchr:near	; CODE XREF: remove_parents+22p
		extrn quote:near	; CODE XREF: remove_parents+69p
					; remove_parents+E3p ...
		extrn prog_fprintf:near	; CODE XREF: remove_parents+90p
					; main+1B9p
; int rmdir(const char *path)
		extrn rmdir:near	; CODE XREF: remove_parents+9Ep
					; main+1C7p
; void error(int status, int errnum, const char	*format, ...)
		extrn error:near	; CODE XREF: remove_parents+10Bp
					; main+159p ...
; struct _IO_FILE *stderr
		extrn stderr:dword	; DATA XREF: usage+25r
; int fprintf(FILE *stream, const char *format,	...)
		extrn fprintf:near	; CODE XREF: usage+30p
; void exit(int	status)
		extrn exit:near		; CODE XREF: usage+F7p	main+FCp ...
		extrn set_program_name:near ; CODE XREF: main+23p
; char *bindtextdomain(const char *domainname, const char *dirname)
		extrn bindtextdomain:near ; CODE XREF: main+4Ap
; char *textdomain(const char *domainname)
		extrn textdomain:near	; CODE XREF: main+5Ap
; void close_stdout(void)
		extrn close_stdout	; DATA XREF: main+65o
; int atexit(void (*func)(void))
		extrn atexit:near	; CODE XREF: main+6Ap
		extrn Version:dword	; DATA XREF: main:loc_80005D6r
		extrn version_etc:near	; CODE XREF: main+EFp
; int getopt_long(int argc, char *const	*argv, const char *shortopts, const struct option *longopts, int *longind)
		extrn getopt_long:near	; CODE XREF: main+11Fp
; int optind
		extrn optind:dword	; DATA XREF: main+134r
					; main:loc_8000673r ...


		end