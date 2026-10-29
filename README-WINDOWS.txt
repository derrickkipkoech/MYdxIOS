DX ARRANGER FOR WINDOWS (no Python needed)
===========================================
START:   double-click Start-DX-Arranger.bat   (or DX-Arranger.exe)
PHONE:   double-click Start-for-phone.bat -> it prints an address and a PIN for your phone/tablet.
         Allow Windows Firewall for PRIVATE networks when asked.

FIRST TIME
 * Windows may say "Windows protected your PC" (the program is not code-signed):
   click More info > Run anyway.
 * FluidSynth and a SoundFont are needed for the good sound. Open config.json (created on first
   run) and set "fluid_exe" and "soundfont" to your own files. Without them the Windows
   built-in synth is used.
 * Put .STY files in the Styles\P01..P16 folders, or import them from the panel.

Everything else works as described in README.txt.
