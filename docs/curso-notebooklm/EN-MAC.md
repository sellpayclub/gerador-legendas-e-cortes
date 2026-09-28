# Install and use from start to finish — Mac

Source document for a narrated lesson. Audience: complete beginners. Pace: calm, one action at a time. Desired length: 10–15 minutes; NotebookLM does not guarantee this duration. Scenes are production instructions, not existing recordings. Described results are expected checks, not evidence of new tests.

## 1. What we will achieve

Suggested visual: Title showing this lesson's operating system; install, configure, export.

Narration:

You will install the Subtitle and Clip Generator on your computer and create your first subtitled video. You do not need programming experience. We will install the app, connect its AI features, and download a finished video. Pause whenever you need more time. The software is open source, with no purchase or mandatory account in local mode. OpenAI API usage is billed separately to your own account. The local address works on the computer running the app; it is not a public website.

Pause / checkpoint: Prepare a 20 to 30 second video with clear speech. Keep your computer powered on and connected to the internet.

## 2. Choose your installation method

Suggested visual: Two cards: an AI assistant with terminal access; the manual installer.

Narration:

If you already use an AI assistant that can run commands on your computer, you can ask it to handle installation. A regular browser conversation may only explain commands; it does not necessarily have access to your computer. Open a local task in your assistant and ask whether it can execute commands on this machine. If it cannot, use the manual alternative in this lesson. You do not need to buy an AI assistant to run the project installer.

Pause / checkpoint: Choose one method. Do not run the manual installer while your assistant is installing the app.

## 3. Find the official project and copy the prompt

Suggested visual: GitHub address and INSTALL-WITH-AI.md, highlighting the complete prompt.

Narration:

Open the repository link supplied with this lesson. Check that the owner is sellpayclub and the repository is gerador-legendas-e-cortes. Open INSTALL-WITH-AI.md in the file list. Select the complete prompt inside its text block, copy it, and paste it into a new local task in your assistant. The prompt asks it to download the project, install dependencies, and check the result. Tell it to preserve your videos and settings if an installation already exists. Do not paste passwords or API keys into the conversation.

Pause / checkpoint: Send the prompt and follow the installation requests. Use the following manual steps if your assistant cannot access a terminal.

## 4. Understand the installation messages

Suggested visual: Python: app service; Node.js: interface; FFmpeg: video processing.

Narration:

You will see download and installation messages. Python runs the service that processes your videos. Node.js prepares the interface. FFmpeg creates the final video with subtitles. The installer handles these dependencies once your operating system's prerequisites are available. The first installation may take several minutes. Wait without closing the window or letting your computer sleep. If an error appears, keep the message instead of repeatedly running unfamiliar commands.

Pause / checkpoint: Wait for completion. The next two scenes explain the manual path for your operating system.

## 5. Manual Mac installation: download and prepare

Suggested visual: Finder, browser, and a permanent folder inside the user's home folder.

Narration:

Skip these two manual scenes if your assistant has already completed installation. Otherwise, click Code and Download ZIP on GitHub. Open the ZIP to extract it. In Finder, choose Go and Home, then move the extracted project folder there. Avoid keeping the installation in Downloads, Desktop, or Documents. Open brew.sh and follow the official Homebrew installation instructions if it is not already installed. Homebrew installs the app's dependencies. If your Mac password is requested, enter it only in the Terminal. Password characters may remain invisible while you type.

Pause / checkpoint: Wait for Homebrew to finish and follow its final instructions to make the brew command available.

## 6. Manual Mac installation: run and reopen

Suggested visual: Terminal: cd and dragged folder path; bash install.sh; ./legendas.sh status.

Narration:

Open Terminal using your Mac's search. Type cd followed by a space, drag the extracted project folder from Finder into Terminal, and press Enter. This selects the correct directory, even when its name contains spaces. Type bash install.sh and press Enter. Wait for downloading and building to finish, then open the local address. To check the services, run ./legendas.sh status from the project folder. To restart, use ./legendas.sh reiniciar. To read diagnostic messages, use ./legendas.sh logs. These script commands keep their original Portuguese spelling even when the interface is English. Services are registered to start when you log in to your Mac; your computer must remain powered on.

Pause / checkpoint: Check the result before proceeding. This is the standard path; troubleshooting depends on the actual error message.

## 7. Open the app and check its services

Suggested visual: Address bar showing http://127.0.0.1:3000, then http://127.0.0.1:8000/api/health.

Narration:

Once installation finishes, open the local address shown by the installer. The default is http://127.0.0.1:3000. Paste it into your browser's address bar, not a search box. You should see the generator's home page. Also open the health address ending in /api/health. This page contains technical text. Look for ok set to true and ffmpeg_ok set to true. These indicate that the service responds and can find FFmpeg. They do not yet prove that transcription and export work. We will test those with a real video.

Pause / checkpoint: If the page does not open, use the troubleshooting scene. Otherwise, proceed to your OpenAI key.

## 8. Connect your own OpenAI account

Suggested visual: platform.openai.com/api-keys; only a masked, fictional key.

Narration:

Open platform.openai.com/api-keys and sign in to your OpenAI platform account. Complete account registration if necessary. In the keys area, choose the option to create a new secret key and give it a recognizable name, such as Local subtitles. Copy it from the platform. This key acts like a password allowing the app to use the API under your account. Check your platform billing setup and API access before your first test. Do not assume your ChatGPT subscription supplies API credit. Never publish the key or include it in a recording.

Pause / checkpoint: Keep the key private and return to the local app to enter it directly in Settings.

## 9. Test and save your key

Suggested visual: Settings → API Key → Test connection → Save; success shown only as an expected outcome.

Narration:

Click Settings at the top of the app. Paste your key in the API Key field. Click Test connection and wait for the result. If the test fails, check the key, API access, and the error message before continuing. If it succeeds, click Save. Testing and saving are separate actions. After saving, the entry field may become blank while the page displays only part of the stored key. That is expected. For your first run, keep OpenAI Whisper selected and leave the alternate base URL blank.

Pause / checkpoint: Confirm that your settings were saved. Never show a complete real key in course screenshots.

## 10. Upload your first video

Suggested visual: Home → Subtitles → audio language → choose file.

Narration:

Return to Home and choose Subtitles. Select the language spoken in the recording, or leave automatic detection enabled. The interface language selector is separate: changing the menu to English does not translate the recording. Click the upload area, choose your short test video, and wait for uploading and transcription. For the first test, use an MP4 with H.264 video and AAC audio. Other formats may upload successfully, but browser playback support varies.

Pause / checkpoint: Wait until the editor shows your video and transcript. Use the troubleshooting section if transcription fails.

## 11. Review and edit subtitles

Suggested visual: Editor showing transcript, style, and subtitle position with neutral sample text.

Narration:

Play the video while reading its words. AI transcription can make mistakes in names, wording, and punctuation, so review the text before exporting. Correct any errors, choose a style, and position the subtitles so they do not cover faces or important content. Keep changes simple for this first test. Check that the preview has picture, sound, and subtitles. Once the basic workflow is verified, you can explore additional styles and effects.

Pause / checkpoint: Continue when the transcript is reviewed and the preview looks correct.

## 12. Render and download the finished video

Suggested visual: Render → completion status → Download MP4 → open downloaded file.

Narration:

Click the video rendering button. Rendering creates a new file with your chosen changes applied. Wait until processing finishes. The time depends on video size and your computer, so there is no single guaranteed duration. When the app reports completion, click Download MP4. Open your browser's downloads list and locate the file. Double-click it to watch outside the app. Check the picture, sound, subtitles, and duration. The test is complete only when the downloaded file plays correctly, not simply when the home page loads.

Pause / checkpoint: Keep the final MP4. If picture, sound, or subtitles are missing, resolve the problem before processing long videos.

## 13. Try the Clips workflow

Suggested visual: Home → Clips → detection → review segments → export.

Narration:

You can also find short segments in a longer recording. Return to Home, select Clips, and upload a video with enough material to select meaningful segments. Run AI detection, review its suggestions, and adjust the start, end, and composition before exporting. A very short video may produce no suggestions, which does not automatically indicate a failure. AI selection is an editorial suggestion: you decide what to publish. Export one clip and open the downloaded file to check the result.

Pause / checkpoint: This is a separate test. A successful subtitled video does not verify every Clips feature.

## 14. Troubleshoot without starting over

Suggested visual: Page unavailable; transcription error; export error.

Narration:

If the page will not open, check its address and use your operating system's restart procedure from this lesson. If transcription fails, test the key in Settings and check API access and billing on the OpenAI platform. If the preview is blank, try H.264 video and AAC audio in an MP4. If rendering fails, ask your assistant to inspect FFmpeg, the ass filter, available disk space, and the logs. Investigate occupied ports rather than closing an unknown program. Copy the error message without exposing any key. Ask your assistant to diagnose the existing installation and preserve your videos while fixing the problem.

Pause / checkpoint: Do not delete the project folder to troubleshoot. Your saved work may be inside it.

## 15. Reopen the app and keep your work

Suggested visual: Browser bookmark and data/jobs/ folder.

Narration:

Bookmark the local address. The app needs your computer powered on and its services running; processing does not continue after shutdown. Your projects are stored in data/jobs inside the installation. Keep exported MP4 files and back up important work. The data/app-settings.json file contains private configuration and must stay out of public uploads. Follow the repository guide when updating, preserving your data. Your installation is validated for this workflow when you can open the app, transcribe, render, and download a playable result.

Pause / checkpoint: Confirm four milestones: home page opens; key is configured; transcription finishes; downloaded MP4 plays correctly.

## Lesson links

- https://github.com/sellpayclub/gerador-legendas-e-cortes
- https://github.com/sellpayclub/gerador-legendas-e-cortes/blob/main/INSTALL-WITH-AI.md
- https://github.com/sellpayclub/gerador-legendas-e-cortes/blob/main/GUIA-INSTALACAO.md
- http://127.0.0.1:3000
- http://127.0.0.1:8000/api/health
- https://platform.openai.com/api-keys
- https://developers.openai.com/api/docs/quickstart
- https://brew.sh
