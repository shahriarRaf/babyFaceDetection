# Model weights (best practice)

This repository's model weights are large binary files (PyTorch `.pt`). You have two main choices:

1) Keep weights out of git and publish them via GitHub Releases or cloud storage (recommended if you don't want LFS).

2) Track weights using Git LFS so they stay with the repo but don't bloat Git history.

Enable Git LFS locally (one-time) and add weights to LFS:

```bash
# install Git LFS (platform-specific installer) and enable it for this repo
git lfs install

# track .pt files (creates/updates .gitattributes)
git lfs track "*.pt"

# add the .gitattributes file already present in this repo
git add .gitattributes

# add your weights and commit (if weights are present locally)
git add baby_detect/weights/*.pt
git commit -m "Add model weights via Git LFS"
git push origin main
```

Notes
- `.gitattributes` already exists in this repository and configures `*.pt` for LFS. You still need to run `git lfs install` on any machine that will push or pull LFS objects.
- If you have already committed `.pt` files without LFS, migrate them into LFS using `git lfs migrate import --include="*.pt"` (this rewrites history — backup first).
- Alternatively, upload weights to a GitHub Release and add a download link and checksum here.
