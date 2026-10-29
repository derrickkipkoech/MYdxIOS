DX ARRANGER FOR ANDROID
=======================
The same panel as the Windows app, with the engine built in (no Python, no server, no FluidSynth, works offline).
It plays DRUMS ONLY, like the Windows app.

GET THE APP (GitHub builds it for you)
  1. Put everything from this package in your GitHub repo (see UPLOAD below).
  2. Open the repo > Actions > "Build Android APK". Wait about 8-12 minutes for the green tick.
  3. Download the APK on your phone, either way:
       - Releases (right side of the repo page) > "DX Arranger for Android (latest)" > DX-Arranger.apk   (easiest)
       - or the run page > Artifacts > DX-Arranger-Android (a zip with the APK inside)
  4. Open DX-Arranger.apk and install. Android will ask you to allow "install unknown apps" for the browser or Files
     app you used: allow it once. Turn the phone sideways (landscape): the panel is wide.
  The Windows build and this build are separate workflows; both can run from the same repo.

FIRST USE
  - Tap once anywhere: Android only lets an app make sound after a touch.
  - Add styles:  press a P button (P1-P16), then the first entry "+ ADD STYLES" > ENTER, choose .STY files from your
    phone. They are stored inside the app (nothing is lost when you close it). Pick a style, ENTER, then START.
  - You can also use INBUILT (import) in the panel's menu: the style is stored and loaded at once.
  - Changing style while playing does not stop the beat: the new one takes over at the next bar at the same tempo.
  - MULTI PADS:  MENU > STYLES > MULTIPAD > "+ ADD FILES" (.wav .mp3 .pad .mid). P1-P4 choose the target pad while the list
    is open (and play it); ENTER loads the highlighted file. Pads loop until you press them again or press STOP.
    STOP stops the beat and every pad. Audio samples loop seamlessly; MIDI pads follow the tempo exactly.
  - EFFECTS: MENU > EFFECTS: Graphic EQ, EQ3-M, EZ EQ, Studio Reverb, Spring Reverb, BL Drive, each with its own ON/OFF and
    ALL EFFECTS OFF. On the phone these are REAL audio effects (real filters, a reverb and a saturation stage).
  - SOUND: MENU > SETTINGS:
      LOAD SOUNDFONT (.SF2)   the same GeneralUser-GS.sf2 as on Windows gives you the same drum sounds. It is stored in the
                              app. Without one the app uses its own built-in synthesized drums.
      USE BUILT-IN SOUNDS     go back to the built-in drums.
      SHAKER LEVEL            100 / 80 / 60 / 40 / 20 %. Default 60% (soft).
      HI-HAT FEEL             on/off: beat strongest, 16ths softest.
      PAD LOOP                on/off.

GOOD TO KNOW
  - The sound stops if the app is sent to the background (Android pauses web audio). Keep it open while you play.
  - The APK is a "debug" build signed with Android's debug key: fine for your own phone, not for the Play Store.
  - Built-in drums are synthesized, so a SoundFont (.sf2) will sound richer. Loading one takes a few seconds.

UPLOAD (GitHub)
  Put these in the repo, keeping the folders:
     android-app/            (whole folder: make_android.py, package.json, capacitor.config.json, www/engine.js, README-ANDROID.txt)
     .github/workflows/build-android.yml
     bridge.js, dxarrangernew1.html and the Windows files as before (the Android app is built from the SAME panel and bridge)
  If the web page will not let you upload the hidden .github folder, use Add file > Create new file, type the name
  .github/workflows/build-android.yml and paste the contents.
