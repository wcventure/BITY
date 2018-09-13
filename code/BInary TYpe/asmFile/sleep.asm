;
; +-------------------------------------------------------------------------+
; |   This file	has been generated by The Interactive Disassembler (IDA)    |
; |	      Copyright	(c) 2015 Hex-Rays, <support@hex-rays.com>	    |
; |			 License info: 48-B611-7234-BB			    |
; |		Doskey Lee, Kingsoft Internet Security Software		    |
; +-------------------------------------------------------------------------+
;
; Input	MD5   :	A6D5E729312CC3C4843032EFFB0B70D2
; Input	CRC32 :	2FA7133E

; File Name   :	D:\coreutils-o\sleep.o
; Format      :	ELF for	Intel 386 (Relocatable)
;
; Source File :	'sleep.c'

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

; void emit_ancillary_info()
emit_ancillary_info proc near		; CODE XREF: usage+A8p

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
		jz	short loc_80000E6
		sub	esp, 4
		push	3		; n
		push	offset s2	; "en_"
		push	[ebp+lc_messages] ; s1
		call	strncmp
		add	esp, 10h
		test	eax, eax
		jz	short loc_80000E6
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

loc_80000E6:				; CODE XREF: emit_ancillary_info+9Bj
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

; Attributes: noreturn bp-based	frame

; void __cdecl usage(int status)
		public usage
usage		proc near		; CODE XREF: main+DBp main+10Ap ...

status		= dword	ptr  8

		push	ebp
		mov	ebp, esp
		push	esi
		push	ebx
		cmp	[ebp+status], 0
		jz	short loc_8000154
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
		jmp	short loc_80001C9
; ---------------------------------------------------------------------------

loc_8000154:				; CODE XREF: usage+9j
		mov	esi, ds:program_name
		mov	ebx, ds:program_name
		sub	esp, 0Ch
		push	offset aUsageSNumberSu ; "Usage: %s NUMBER[SUFFIX]...\n	 or:  %s "...
		call	gettext
		add	esp, 10h
		sub	esp, 4
		push	esi
		push	ebx
		push	eax		; format
		call	printf
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

loc_80001C9:				; CODE XREF: usage+36j
		sub	esp, 0Ch
		push	[ebp+status]	; status
		call	exit
usage		endp


; =============== S U B	R O U T	I N E =======================================

; Attributes: static bp-based frame

; _Bool	__cdecl	apply_suffix(double *x,	char suffix_char)
apply_suffix	proc near		; CODE XREF: main+187p

suffix_char	= byte ptr -14h
multiplier	= dword	ptr -4
x		= dword	ptr  8
arg_4		= dword	ptr  0Ch

		push	ebp
		mov	ebp, esp
		sub	esp, 18h
		mov	eax, [ebp+arg_4]
		mov	[ebp+suffix_char], al
		movsx	eax, [ebp+suffix_char]
		cmp	eax, 68h
		jz	short loc_8000215
		cmp	eax, 68h
		jg	short loc_80001F9
		test	eax, eax
		jz	short loc_8000203
		cmp	eax, 64h
		jz	short loc_800021E
		jmp	short loc_8000227
; ---------------------------------------------------------------------------

loc_80001F9:				; CODE XREF: apply_suffix+18j
		cmp	eax, 6Dh
		jz	short loc_800020C
		cmp	eax, 73h
		jnz	short loc_8000227

loc_8000203:				; CODE XREF: apply_suffix+1Cj
		mov	[ebp+multiplier], 1
		jmp	short loc_800022E
; ---------------------------------------------------------------------------

loc_800020C:				; CODE XREF: apply_suffix+28j
		mov	[ebp+multiplier], 3Ch
		jmp	short loc_800022E
; ---------------------------------------------------------------------------

loc_8000215:				; CODE XREF: apply_suffix+13j
		mov	[ebp+multiplier], 0E10h
		jmp	short loc_800022E
; ---------------------------------------------------------------------------

loc_800021E:				; CODE XREF: apply_suffix+21j
		mov	[ebp+multiplier], 15180h
		jmp	short loc_800022E
; ---------------------------------------------------------------------------

loc_8000227:				; CODE XREF: apply_suffix+23j
					; apply_suffix+2Dj
		mov	eax, 0
		jmp	short locret_8000242
; ---------------------------------------------------------------------------

loc_800022E:				; CODE XREF: apply_suffix+36j
					; apply_suffix+3Fj ...
		mov	eax, [ebp+x]
		fld	qword ptr [eax]
		fild	[ebp+multiplier]
		fmulp	st(1), st
		mov	eax, [ebp+x]
		fstp	qword ptr [eax]
		mov	eax, 1

locret_8000242:				; CODE XREF: apply_suffix+58j
		leave
		retn
apply_suffix	endp


; =============== S U B	R O U T	I N E =======================================

; Attributes: noreturn bp-based	frame

; int __cdecl main(int argc, const char	**argv,	const char **envp)
		public main
main		proc near

argv		= dword	ptr -4Ch
ok		= byte ptr -39h
p		= dword	ptr -38h
i		= dword	ptr -34h
s		= qword	ptr -30h
seconds		= qword	ptr -28h
var_1C		= dword	ptr -1Ch
argc		= dword	ptr  0Ch
envp		= dword	ptr  14h

		lea	ecx, [esp+4]
		and	esp, 0FFFFFFF0h
		push	dword ptr [ecx-4]
		push	ebp
		mov	ebp, esp
		push	esi
		push	ebx
		push	ecx
		sub	esp, 4Ch
		mov	ebx, ecx
		mov	eax, [ebx+4]
		mov	[ebp+argv], eax
		mov	eax, large gs:14h
		mov	[ebp+var_1C], eax
		xor	eax, eax
		fldz
		fstp	[ebp+seconds]
		mov	[ebp+ok], 1
		mov	eax, [ebp+argv]
		mov	eax, [eax]
		sub	esp, 0Ch
		push	eax
		call	set_program_name
		add	esp, 10h
		sub	esp, 8
		push	offset shortopts ; locale
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
		mov	eax, ds:Version
		sub	esp, 0Ch
		push	0
		push	offset aPaulEggert ; "Paul Eggert"
		push	offset aJimMeyering ; "Jim Meyering"
		push	offset usage
		push	eax
		push	offset aGnuCoreutils ; "GNU coreutils"
		push	offset aSleep	; "sleep"
		push	[ebp+argv]
		push	dword ptr [ebx]
		call	parse_long_options
		add	esp, 30h
		sub	esp, 0Ch
		push	0		; longind
		push	0		; longopts
		push	offset shortopts ; shortopts
		push	[ebp+argv]	; argv
		push	dword ptr [ebx]	; argc
		call	getopt_long
		add	esp, 20h
		cmp	eax, 0FFFFFFFFh
		jz	short loc_8000324
		sub	esp, 0Ch
		push	1		; status
		call	usage
; ---------------------------------------------------------------------------

loc_8000324:				; CODE XREF: main+D4j
		cmp	dword ptr [ebx], 1
		jnz	short loc_8000353
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

loc_8000353:				; CODE XREF: main+E3j
		mov	eax, ds:optind
		mov	[ebp+i], eax
		jmp	loc_800042A
; ---------------------------------------------------------------------------

loc_8000360:				; CODE XREF: main+1EBj
		mov	eax, [ebp+i]
		lea	edx, ds:0[eax*4]
		mov	eax, [ebp+argv]
		add	eax, edx
		mov	eax, [eax]
		push	offset c_strtod
		lea	edx, [ebp+s]
		push	edx
		lea	edx, [ebp+p]
		push	edx
		push	eax
		call	xstrtod
		add	esp, 10h
		xor	eax, 1
		test	al, al
		jnz	short loc_80003DA
		fld	[ebp+s]
		fldz
		fxch	st(1)
		fucomip	st, st(1)
		fstp	st
		setnb	al
		xor	eax, 1
		test	al, al
		jnz	short loc_80003DA
		mov	eax, [ebp+p]
		movzx	eax, byte ptr [eax]
		test	al, al
		jz	short loc_80003BA
		mov	eax, [ebp+p]
		add	eax, 1
		movzx	eax, byte ptr [eax]
		test	al, al
		jnz	short loc_80003DA

loc_80003BA:				; CODE XREF: main+167j
		mov	eax, [ebp+p]
		movzx	eax, byte ptr [eax]
		movsx	eax, al
		sub	esp, 8
		push	eax		; suffix_char
		lea	eax, [ebp+s]
		push	eax		; x
		call	apply_suffix
		add	esp, 10h
		xor	eax, 1
		test	al, al
		jz	short loc_800041B

loc_80003DA:				; CODE XREF: main+148j	main+15Dj ...
		mov	eax, [ebp+i]
		lea	edx, ds:0[eax*4]
		mov	eax, [ebp+argv]
		add	eax, edx
		mov	eax, [eax]
		sub	esp, 0Ch
		push	eax
		call	quote
		add	esp, 10h
		mov	esi, eax
		sub	esp, 0Ch
		push	offset aInvalidTimeInt ; "invalid time interval	%s"
		call	gettext
		add	esp, 10h
		push	esi
		push	eax		; format
		push	0		; errnum
		push	0		; status
		call	error
		add	esp, 10h
		mov	[ebp+ok], 0

loc_800041B:				; CODE XREF: main+194j
		fld	[ebp+s]
		fld	[ebp+seconds]
		faddp	st(1), st
		fstp	[ebp+seconds]
		add	[ebp+i], 1

loc_800042A:				; CODE XREF: main+117j
		mov	eax, [ebp+i]
		cmp	eax, [ebx]
		jl	loc_8000360
		movzx	eax, [ebp+ok]
		xor	eax, 1
		test	al, al
		jz	short loc_800044A
		sub	esp, 0Ch
		push	1		; status
		call	usage
; ---------------------------------------------------------------------------

loc_800044A:				; CODE XREF: main+1FAj
		sub	esp, 8
		push	dword ptr [ebp+seconds+4]
		push	dword ptr [ebp+seconds]
		call	xnanosleep
		add	esp, 10h
		test	eax, eax
		jz	short loc_8000487
		sub	esp, 0Ch
		push	offset aCannotReadReal ; "cannot read realtime clock"
		call	gettext
		add	esp, 10h
		mov	ebx, eax
		call	__errno_location
		mov	eax, [eax]
		sub	esp, 4
		push	ebx		; format
		push	eax		; errnum
		push	1		; status
		call	error
		add	esp, 10h

loc_8000487:				; CODE XREF: main+219j
		sub	esp, 0Ch
		push	0		; status

loc_800048C:				; DATA XREF: .eh_frame:0800088Co
					; .eh_frame:080008B0o ...
		call	exit
main		endp

_text		ends

; ===========================================================================

; Segment type:	Zero-length
; Segment permissions: Read/Write
_data		segment	byte public 'DATA' use32
_data		ends

; ===========================================================================

; Segment type:	Zero-length
; Segment permissions: Read/Write
_bss		segment	byte public 'BSS' use32
_bss		ends

; ===========================================================================

; Segment type:	Pure data
; Segment permissions: Read
_rodata		segment	dword public 'CONST' use32
		assume cs:_rodata
		;org 8000494h
; char msgid[]
msgid		db 0Ah			; DATA XREF: emit_ancillary_info+1Do
		db 'Report %s bugs to %s',0Ah,0
aBugCoreutils@g	db 'bug-coreutils@gnu.org',0 ; DATA XREF: emit_ancillary_info+2Do
		align 4
; char aSHomePageHttpW[]
aSHomePageHttpW	db '%s home page: <http://www.gnu.org/software/%s/>',0Ah,0
					; DATA XREF: emit_ancillary_info+3Fo
; char domainname[]
domainname	db 'coreutils',0        ; DATA XREF: emit_ancillary_info+4Fo
					; main+5Ao ...
aGnuCoreutils	db 'GNU coreutils',0    ; DATA XREF: emit_ancillary_info+54o
					; main+A1o
		align 10h
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
		align 10h
; char aTrySHelpForMor[]
aTrySHelpForMor	db 'Try `%s --help',27h,' for more information.',0Ah,0
					; DATA XREF: usage+14o
		align 4
; char aUsageSNumberSu[]
aUsageSNumberSu	db 'Usage: %s NUMBER[SUFFIX]...',0Ah ; DATA XREF: usage+47o
		db '  or:  %s OPTION',0Ah
		db 'Pause for NUMBER seconds.  SUFFIX may be `s',27h,' for seconds (the '
		db 'default),',0Ah
		db '`m',27h,' for minutes, `h',27h,' for hours or `d',27h,' for days.  Unlike '
		db 'most implementations',0Ah
		db 'that require NUMBER be an integer, here NUMBER may be an arbitrar'
		db 'y floating',0Ah
		db 'point number.  Given two or more arguments, pause for the amount '
		db 'of time',0Ah
		db 'specified by the sum of their values.',0Ah
		db 0Ah,0
		align 4
; char aHelpDisplayThi[]
aHelpDisplayThi	db '      --help     display this help and exit',0Ah,0
					; DATA XREF: usage+6Bo
		align 4
; char aVersionOutputV[]
aVersionOutputV	db '      --version  output version information and exit',0Ah,0
					; DATA XREF: usage+8Eo
; char shortopts
shortopts	db 0			; DATA XREF: main+43o main+BFo
; char dirname[]
dirname		db '/usr/local/share/locale',0 ; DATA XREF: main+55o
aPaulEggert	db 'Paul Eggert',0      ; DATA XREF: main+91o
aJimMeyering	db 'Jim Meyering',0     ; DATA XREF: main+96o
aSleep		db 'sleep',0            ; DATA XREF: main+A6o
; char aMissingOperand[]
aMissingOperand	db 'missing operand',0  ; DATA XREF: main+E8o
; char aInvalidTimeInt[]
aInvalidTimeInt	db 'invalid time interval %s',0 ; DATA XREF: main+1B8o
; char aCannotReadReal[]
aCannotReadReal	db 'cannot read realtime clock',0 ; DATA XREF: main+21Eo
_rodata		ends

; ===========================================================================

; Segment type:	Pure data
; Segment permissions: Read
_eh_frame	segment	dword public 'CONST' use32
		assume cs:_eh_frame
		;org 800086Ch
		dd 14h,	0
		dd 527A01h, 1087C01h, 4040C1Bh,	188h, 20h, 1Ch
		dd offset loc_800048C-8000D18h
		dd 11Ch, 80E4100h, 0D420285h, 3834405h,	0C5011403h, 4040CC3h
		dd 1Ch,	40h
		dd offset loc_800048C-8000C20h
		dd 0B8h, 80E4100h, 0D420285h, 3864205h,	483h, 1Ch, 60h
		dd offset loc_800048C-8000B88h
		dd 70h,	80E4100h, 0D420285h, 0C56C0205h, 4040Ch, 28h, 80h
		dd offset loc_800048C-8000B38h
		dd 24Dh, 10C4400h, 5104700h, 45007502h,	7475030Fh, 2061006h
		dd 3107C75h, 787502h
_eh_frame	ends

; ===========================================================================

; Segment type:	Externs
; extern
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
					; usage+62r ...
		extrn fputs_unlocked:near ; CODE XREF: emit_ancillary_info+7Dp
					; usage+7Dp ...
; char *setlocale(int category,	const char *locale)
		extrn setlocale:near	; CODE XREF: emit_ancillary_info+8Cp
					; main+4Ap
; int strncmp(const char *s1, const char *s2, size_t n)
		extrn strncmp:near	; CODE XREF: emit_ancillary_info+AAp
; struct _IO_FILE *stderr
		extrn stderr:dword	; DATA XREF: usage+23r
; int fprintf(FILE *stream, const char *format,	...)
		extrn fprintf:near	; CODE XREF: usage+2Ep
; void exit(int	status)
		extrn exit:near		; CODE XREF: usage+B3p
					; main:loc_800048Cp
		extrn set_program_name:near ; CODE XREF: main+38p
; char *bindtextdomain(const char *domainname, const char *dirname)
		extrn bindtextdomain:near ; CODE XREF: main+5Fp
; char *textdomain(const char *domainname)
		extrn textdomain:near	; CODE XREF: main+6Fp
; void close_stdout(void)
		extrn close_stdout	; DATA XREF: main+7Ao
; int atexit(void (*func)(void))
		extrn atexit:near	; CODE XREF: main+7Fp
		extrn Version:dword	; DATA XREF: main+87r
		extrn parse_long_options:near ;	CODE XREF: main+B0p
; int getopt_long(int argc, char *const	*argv, const char *shortopts, const struct option *longopts, int *longind)
		extrn getopt_long:near	; CODE XREF: main+C9p
; void error(int status, int errnum, const char	*format, ...)
		extrn error:near	; CODE XREF: main+FDp main+1CBp ...
; int optind
		extrn optind:dword	; DATA XREF: main:loc_8000353r
		extrn c_strtod		; DATA XREF: main+12Do
		extrn xstrtod:near	; CODE XREF: main+13Bp
		extrn quote:near	; CODE XREF: main+1ABp
		extrn xnanosleep:near	; CODE XREF: main+20Fp
; int *_errno_location(void)
		extrn __errno_location:near ; CODE XREF: main+22Dp


		end