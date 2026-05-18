# Important: Repository history rewritten — action required

I migrated `*.pt` model weight files into Git LFS and force-pushed rewritten history to the remote. This rewrote commits on `main` and added LFS support for weights.

If you previously cloned this repository, follow these steps to resynchronize safely:

1) Save any local changes (if present)

   - Commit them on a throwaway branch, or create a patch:

     ```bash
     git checkout -b my-wip-branch
     git add -A
     git commit -m "WIP: save local changes before repo rewrite"
     ```

2) Remove the existing local clone (recommended) and re-clone

   ```bash
   # optional: move the old clone out of the way
   cd ..
   mv babyFaceDetection babyFaceDetection.old

   # clone fresh
   git clone https://github.com/shahriarRaf/babyFaceDetection.git
   cd babyFaceDetection
   git lfs install
   git lfs pull
   ```

3) If you cannot reclone, you can reset your local repo (advanced)

   ```bash
   git fetch origin
   git checkout main
   git reset --hard origin/main
   git lfs install
   git lfs pull
   ```

4) After re-cloning, restore any saved WIP changes by cherry-picking or merging your WIP branch.

Security note
- If you had ever committed `service-account.json` or other credentials and pushed them prior to cleanup, rotate those keys immediately. Treat any pushed credentials as compromised.

Contact
- If you need help migrating your local clone safely or restoring WIP changes, open an issue or contact the repo owner.
