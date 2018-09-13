;
; +-------------------------------------------------------------------------+
; |   This file	has been generated by The Interactive Disassembler (IDA)    |
; |	      Copyright	(c) 2015 Hex-Rays, <support@hex-rays.com>	    |
; |			 License info: 48-B611-7234-BB			    |
; |		Doskey Lee, Kingsoft Internet Security Software		    |
; +-------------------------------------------------------------------------+
;
; Input	MD5   :	2935ACB35ABE6D697CFE3B338DFBE1EA
; Input	CRC32 :	BECC0969

; File Name   :	D:\coreutils-o\readlink.o
; Format      :	ELF for	Intel 386 (Relocatable)
;
; Source File :	'readlink.c'

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
emit_ancillary_info proc near		; CODE XREF: usage+10Fp

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
usage		proc near		; CODE XREF: main+106p	main+143p ...

status		= dword	ptr  8

		push	ebp
		mov	ebp, esp
		push	ebx
		sub	esp, 4
		cmp	[ebp+status], 0
		jz	short loc_8000159
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
		jmp	loc_8000230
; ---------------------------------------------------------------------------

loc_8000159:				; CODE XREF: usage+Bj
		mov	ebx, ds:program_name
		sub	esp, 0Ch
		push	offset aUsageSOption__ ; "Usage: %s [OPTION]...	FILE\n"
		call	gettext
		add	esp, 10h
		sub	esp, 8
		push	ebx
		push	eax		; format
		call	printf
		add	esp, 10h
		mov	ebx, ds:stdout
		sub	esp, 0Ch
		push	offset aPrintValueOfAS ; "Print	value of a symbolic link or canon"...
		call	gettext
		add	esp, 10h
		sub	esp, 8
		push	ebx
		push	eax
		call	fputs_unlocked
		add	esp, 10h
		mov	ebx, ds:stdout
		sub	esp, 0Ch
		push	offset aFCanonicalizeC ; "  -f,	--canonicalize		  canonic"...
		call	gettext
		add	esp, 10h
		sub	esp, 8
		push	ebx
		push	eax
		call	fputs_unlocked
		add	esp, 10h
		mov	ebx, ds:stdout
		sub	esp, 0Ch
		push	offset aMCanonicalizeM ; "  -m,	--canonicalize-missing	  canonic"...
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

loc_8000230:				; CODE XREF: usage+38j
		sub	esp, 0Ch
		push	[ebp+status]	; status
		call	exit
usage		endp


; =============== S U B	R O U T	I N E =======================================

; Attributes: bp-based frame

; int __cdecl main(int argc, const char	**argv,	const char **envp)
		public main
main		proc near

can_mode	= dword	ptr -18h
optc		= dword	ptr -14h
fname		= dword	ptr -10h
value		= dword	ptr -0Ch
argc		= dword	ptr  0Ch
argv		= dword	ptr  10h
envp		= dword	ptr  14h

		lea	ecx, [esp+4]
		and	esp, 0FFFFFFF0h
		push	dword ptr [ecx-4]
		push	ebp
		mov	ebp, esp
		push	ebx
		push	ecx
		sub	esp, 10h
		mov	ebx, ecx
		mov	[ebp+can_mode],	0FFFFFFFFh
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
		jmp	loc_8000383
; ---------------------------------------------------------------------------

loc_80002B3:				; CODE XREF: main+16Bj
		mov	eax, [ebp+optc]
		cmp	eax, 6Dh
		jz	short loc_8000318
		cmp	eax, 6Dh
		jg	short loc_80002E9
		cmp	eax, 0FFFFFF7Eh
		jz	short loc_800033C
		cmp	eax, 0FFFFFF7Eh
		jg	short loc_80002DA
		cmp	eax, 0FFFFFF7Dh
		jz	short loc_8000346
		jmp	loc_8000379
; ---------------------------------------------------------------------------

loc_80002DA:				; CODE XREF: main+91j
		cmp	eax, 65h
		jz	short loc_8000306
		cmp	eax, 66h
		jz	short loc_800030F
		jmp	loc_8000379
; ---------------------------------------------------------------------------

loc_80002E9:				; CODE XREF: main+83j
		cmp	eax, 71h
		jz	short loc_800032A
		cmp	eax, 71h
		jg	short loc_80002FA
		cmp	eax, 6Eh
		jz	short loc_8000321
		jmp	short loc_8000379
; ---------------------------------------------------------------------------

loc_80002FA:				; CODE XREF: main+B6j
		cmp	eax, 73h
		jz	short loc_800032A
		cmp	eax, 76h
		jz	short loc_8000333
		jmp	short loc_8000379
; ---------------------------------------------------------------------------

loc_8000306:				; CODE XREF: main+A2j
		mov	[ebp+can_mode],	0
		jmp	short loc_8000383
; ---------------------------------------------------------------------------

loc_800030F:				; CODE XREF: main+A7j
		mov	[ebp+can_mode],	1
		jmp	short loc_8000383
; ---------------------------------------------------------------------------

loc_8000318:				; CODE XREF: main+7Ej
		mov	[ebp+can_mode],	2
		jmp	short loc_8000383
; ---------------------------------------------------------------------------

loc_8000321:				; CODE XREF: main+BBj
		mov	ds:no_newline, 1
		jmp	short loc_8000383
; ---------------------------------------------------------------------------

loc_800032A:				; CODE XREF: main+B1j main+C2j
		mov	ds:verbose, 0
		jmp	short loc_8000383
; ---------------------------------------------------------------------------

loc_8000333:				; CODE XREF: main+C7j
		mov	ds:verbose, 1
		jmp	short loc_8000383
; ---------------------------------------------------------------------------

loc_800033C:				; CODE XREF: main+8Aj
		sub	esp, 0Ch
		push	0		; status
		call	usage
; ---------------------------------------------------------------------------

loc_8000346:				; CODE XREF: main+98j
		mov	edx, ds:Version
		mov	eax, ds:stdout
		sub	esp, 8
		push	0
		push	offset aDmitryV_Levin ;	"Dmitry	V. Levin"
		push	edx
		push	offset aGnuCoreutils ; "GNU coreutils"
		push	offset aReadlink ; "readlink"
		push	eax
		call	version_etc
		add	esp, 20h
		sub	esp, 0Ch
		push	0		; status
		call	exit
; ---------------------------------------------------------------------------

loc_8000379:				; CODE XREF: main+9Aj main+A9j ...
		sub	esp, 0Ch
		push	1		; status
		call	usage
; ---------------------------------------------------------------------------

loc_8000383:				; CODE XREF: main+73j main+D2j ...
		sub	esp, 0Ch
		push	0		; longind
		push	offset longopts	; longopts
		push	offset shortopts ; "efmnqsv"
		push	dword ptr [ebx+4] ; argv
		push	dword ptr [ebx]	; argc
		call	getopt_long
		add	esp, 20h
		mov	[ebp+optc], eax
		cmp	[ebp+optc], 0FFFFFFFFh
		jnz	loc_80002B3
		mov	eax, ds:optind
		cmp	eax, [ebx]
		jl	short loc_80003DF
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

loc_80003DF:				; CODE XREF: main+178j
		mov	eax, ds:optind
		lea	edx, [eax+1]
		mov	ds:optind, edx
		lea	edx, ds:0[eax*4]
		mov	eax, [ebx+4]
		add	eax, edx
		mov	eax, [eax]
		mov	[ebp+fname], eax
		mov	eax, ds:optind
		cmp	eax, [ebx]
		jge	short loc_8000450
		mov	eax, ds:optind
		lea	edx, ds:0[eax*4]
		mov	eax, [ebx+4]
		add	eax, edx
		mov	eax, [eax]
		sub	esp, 0Ch
		push	eax
		call	quote
		add	esp, 10h
		mov	ebx, eax
		sub	esp, 0Ch
		push	offset aExtraOperandS ;	"extra operand %s"
		call	gettext
		add	esp, 10h
		push	ebx
		push	eax		; format
		push	0		; errnum
		push	0		; status
		call	error
		add	esp, 10h
		sub	esp, 0Ch
		push	1		; status
		call	usage
; ---------------------------------------------------------------------------

loc_8000450:				; CODE XREF: main+1CAj
		cmp	[ebp+can_mode],	0FFFFFFFFh
		jz	short loc_800046A
		mov	eax, [ebp+can_mode]
		sub	esp, 8
		push	eax
		push	[ebp+fname]
		call	canonicalize_filename_mode
		add	esp, 10h
		jmp	short loc_800047A
; ---------------------------------------------------------------------------

loc_800046A:				; CODE XREF: main+219j
		sub	esp, 8
		push	3Fh
		push	[ebp+fname]
		call	areadlink_with_size
		add	esp, 10h

loc_800047A:				; CODE XREF: main+22Dj
		mov	[ebp+value], eax
		cmp	[ebp+value], 0
		jz	short loc_80004C3
		movzx	eax, ds:no_newline
		test	al, al
		jz	short loc_8000495
		mov	eax, offset locale
		jmp	short loc_800049A
; ---------------------------------------------------------------------------

loc_8000495:				; CODE XREF: main+251j
		mov	eax, offset asc_8000C05	; "\n"

loc_800049A:				; CODE XREF: main+258j
		sub	esp, 4
		push	eax
		push	[ebp+value]
		push	offset format	; "%s%s"
		call	printf
		add	esp, 10h
		sub	esp, 0Ch
		push	[ebp+value]	; ptr
		call	free
		add	esp, 10h
		mov	eax, 0
		jmp	short loc_80004ED
; ---------------------------------------------------------------------------

loc_80004C3:				; CODE XREF: main+246j
		movzx	eax, ds:verbose
		test	al, al
		jz	short loc_80004E8
		call	__errno_location
		mov	eax, [eax]
		push	[ebp+fname]
		push	offset aS	; "%s"
		push	eax		; errnum
		push	1		; status
		call	error
		add	esp, 10h

loc_80004E8:				; CODE XREF: main+291j
		mov	eax, 1

loc_80004ED:				; CODE XREF: main+286j
		lea	esp, [ebp-8]
		pop	ecx
		pop	ebx
		pop	ebp
		lea	esp, [ecx-4]

locret_80004F6:				; DATA XREF: .eh_frame:08000C30o
					; .eh_frame:08000C54o ...
		retn
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
		;org 80004F8h
		assume es:nothing, ss:nothing, ds:_text, fs:nothing, gs:nothing
; _Bool	no_newline
no_newline	db ?			; DATA XREF: main:loc_8000321w
					; main+248r
; _Bool	verbose
verbose		db ?			; DATA XREF: main:loc_800032Aw
					; main:loc_8000333w ...
_bss		ends

; ===========================================================================

; Segment type:	Pure data
; Segment permissions: Read
; Segment alignment '32byte' can not be represented in assembly
_rodata		segment	para public 'CONST' use32
		assume cs:_rodata
		;org 8000500h
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
					; main+46o ...
aGnuCoreutils	db 'GNU coreutils',0    ; DATA XREF: emit_ancillary_info+54o
					; main+121o
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
aCanonicalize	db 'canonicalize',0     ; DATA XREF: .rodata:longoptso
aCanonicalizeEx	db 'canonicalize-existing',0 ; DATA XREF: .rodata:longoptso
aCanonicalizeMi	db 'canonicalize-missing',0 ; DATA XREF: .rodata:longoptso
aNoNewline	db 'no-newline',0       ; DATA XREF: .rodata:longoptso
aQuiet		db 'quiet',0            ; DATA XREF: .rodata:longoptso
aSilent		db 'silent',0           ; DATA XREF: .rodata:longoptso
aVerbose	db 'verbose',0          ; DATA XREF: .rodata:longoptso
aHelp		db 'help',0             ; DATA XREF: .rodata:longoptso
aVersion	db 'version',0          ; DATA XREF: .rodata:longoptso
		align 20h
; const	option longopts[10]
longopts	option <offset aCanonicalize, 0, 0, 66h> ; DATA	XREF: main+14Do
		option <offset aCanonicalizeEx,	0, 0, 65h> ; "canonicalize"
		option <offset aCanonicalizeMi,	0, 0, 6Dh>
		option <offset aNoNewline, 0, 0, 6Eh>
		option <offset aQuiet, 0, 0, 71h>
		option <offset aSilent,	0, 0, 73h>
		option <offset aVerbose, 0, 0, 76h>
		option <offset aHelp, 0, 0, 0FFFFFF7Eh>
		option <offset aVersion, 0, 0, 0FFFFFF7Dh>
		option	<0>
; char aTrySHelpForMor[]
aTrySHelpForMor	db 'Try `%s --help',27h,' for more information.',0Ah,0
					; DATA XREF: usage+16o
; char aUsageSOption__[]
aUsageSOption__	db 'Usage: %s [OPTION]... FILE',0Ah,0 ; DATA XREF: usage+46o
		align 4
; char aPrintValueOfAS[]
aPrintValueOfAS	db 'Print value of a symbolic link or canonical file name',0Ah
					; DATA XREF: usage+69o
		db 0Ah,0
; char aFCanonicalizeC[]
aFCanonicalizeC	db '  -f, --canonicalize            canonicalize by following every s'
					; DATA XREF: usage+8Co
		db 'ymlink in',0Ah
		db '                                every component of the given name'
		db ' recursively;',0Ah
		db '                                all but the last component must e'
		db 'xist',0Ah
		db '  -e, --canonicalize-existing   canonicalize by following every s'
		db 'ymlink in',0Ah
		db '                                every component of the given name'
		db ' recursively,',0Ah
		db '                                all components must exist',0Ah,0
		align 4
; char aMCanonicalizeM[]
aMCanonicalizeM	db '  -m, --canonicalize-missing    canonicalize by following every s'
					; DATA XREF: usage+AFo
		db 'ymlink in',0Ah
		db '                                every component of the given name'
		db ' recursively,',0Ah
		db '                                without requirements on component'
		db 's existence',0Ah
		db '  -n, --no-newline              do not output the trailing newlin'
		db 'e',0Ah
		db '  -q, --quiet,',0Ah
		db '  -s, --silent                  suppress most error messages',0Ah
		db '  -v, --verbose                 report error messages',0Ah,0
		align 4
; char aHelpDisplayThi[]
aHelpDisplayThi	db '      --help     display this help and exit',0Ah,0
					; DATA XREF: usage+D2o
		align 4
; char aVersionOutputV[]
aVersionOutputV	db '      --version  output version information and exit',0Ah,0
					; DATA XREF: usage+F5o
; char locale
locale		db 0			; DATA XREF: main+2Fo main+253o
; char dirname[]
dirname		db '/usr/local/share/locale',0 ; DATA XREF: main+41o
aDmitryV_Levin	db 'Dmitry V. Levin',0  ; DATA XREF: main+11Bo
aReadlink	db 'readlink',0         ; DATA XREF: main+126o
; char shortopts[]
shortopts	db 'efmnqsv',0          ; DATA XREF: main+152o
; char aMissingOperand[]
aMissingOperand	db 'missing operand',0  ; DATA XREF: main+17Do
; char aExtraOperandS[]
aExtraOperandS	db 'extra operand %s',0 ; DATA XREF: main+1F0o
asc_8000C05	db 0Ah,0		; DATA XREF: main:loc_8000495o
; char format[]
format		db '%s%s',0             ; DATA XREF: main+266o
; char aS[]
aS		db '%s',0               ; DATA XREF: main+29Do
_rodata		ends

; ===========================================================================

; Segment type:	Pure data
; Segment permissions: Read
_eh_frame	segment	dword public 'CONST' use32
		assume cs:_eh_frame
		;org 8000C10h
		dd 14h,	0
		dd 527A01h, 1087C01h, 4040C1Bh,	188h, 20h, 1Ch
		dd offset locret_80004F6-8001126h
		dd 11Ch, 80E4100h, 0D420285h, 3834405h,	0C5011403h, 4040CC3h
		dd 18h,	40h
		dd offset locret_80004F6-800102Eh
		dd 11Fh, 80E4100h, 0D420285h, 3834405h,	34h, 5Ch
		dd offset locret_80004F6-8000F2Bh
		dd 2BCh, 10C4400h, 5104700h, 44007502h,	7875030Fh, 2031006h
		dd 0A7037C75h, 10CC102h, 41C34100h, 40C43C5h, 4
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
					; usage+60r ...
		extrn fputs_unlocked:near ; CODE XREF: emit_ancillary_info+7Dp
					; usage+7Bp ...
; char *setlocale(int category,	const char *locale)
		extrn setlocale:near	; CODE XREF: emit_ancillary_info+8Cp
					; main+36p
; int strncmp(const char *s1, const char *s2, size_t n)
		extrn strncmp:near	; CODE XREF: emit_ancillary_info+AAp
; struct _IO_FILE *stderr
		extrn stderr:dword	; DATA XREF: usage+25r
; int fprintf(FILE *stream, const char *format,	...)
		extrn fprintf:near	; CODE XREF: usage+30p
; void exit(int	status)
		extrn exit:near		; CODE XREF: usage+11Ap main+139p
		extrn set_program_name:near ; CODE XREF: main+24p
; char *bindtextdomain(const char *domainname, const char *dirname)
		extrn bindtextdomain:near ; CODE XREF: main+4Bp
; char *textdomain(const char *domainname)
		extrn textdomain:near	; CODE XREF: main+5Bp
; void close_stdout(void)
		extrn close_stdout	; DATA XREF: main+66o
; int atexit(void (*func)(void))
		extrn atexit:near	; CODE XREF: main+6Bp
		extrn Version:dword	; DATA XREF: main:loc_8000346r
		extrn version_etc:near	; CODE XREF: main+12Cp
; int getopt_long(int argc, char *const	*argv, const char *shortopts, const struct option *longopts, int *longind)
		extrn getopt_long:near	; CODE XREF: main+15Cp
; int optind
		extrn optind:dword	; DATA XREF: main+171r
					; main:loc_80003DFr ...
; void error(int status, int errnum, const char	*format, ...)
		extrn error:near	; CODE XREF: main+192p	main+203p ...
		extrn quote:near	; CODE XREF: main+1E3p
		extrn canonicalize_filename_mode:near ;	CODE XREF: main+225p
		extrn areadlink_with_size:near ; CODE XREF: main+237p
; void free(void *ptr)
		extrn free:near		; CODE XREF: main+279p
; int *_errno_location(void)
		extrn __errno_location:near ; CODE XREF: main+293p


		end