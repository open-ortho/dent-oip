{
  description = "Development shell for building the DENT-OIP Sphinx documentation";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
        runtimeLibraryPath = pkgs.lib.makeLibraryPath [
          pkgs.stdenv.cc.cc.lib
          pkgs.zlib
        ];
      in
      {
        devShells.default = pkgs.mkShell {
          packages = [
            pkgs.coreutils
            pkgs.git
            pkgs.gnumake
            pkgs.gnused
            pkgs.python3
          ];

          shellHook = ''
            requirements_file="$PWD/requirements.txt"

            if [ ! -f "$requirements_file" ]; then
              echo "requirements.txt not found; run nix develop from the repository root." >&2
              return 1 2>/dev/null || exit 1
            fi

            project_hash="$(printf '%s' "$PWD" | sha256sum | cut -d ' ' -f 1)"
            requirements_hash="$(sha256sum "$requirements_file" | cut -d ' ' -f 1)"
            cache_dir="''${XDG_CACHE_HOME:-$HOME/.cache}/dent-oip"
            venv_dir="$cache_dir/nix-venv-$project_hash"
            marker_file="$venv_dir/.requirements-hash"

            if [ ! -x "$venv_dir/bin/sphinx-build" ] || [ "$(cat "$marker_file" 2>/dev/null)" != "$requirements_hash" ]; then
              echo "Preparing Python virtualenv for DENT-OIP..."
              if ! (
                set -e
                rm -rf "$venv_dir"
                mkdir -p "$cache_dir"
                python3 -m venv "$venv_dir"
                "$venv_dir/bin/python" -m pip install --upgrade pip
                "$venv_dir/bin/python" -m pip install -r "$requirements_file"
                printf '%s' "$requirements_hash" > "$marker_file"
              ); then
                echo "Failed to prepare the DENT-OIP Python virtualenv." >&2
                return 1 2>/dev/null || exit 1
              fi
            fi

            export PATH="$venv_dir/bin:$PATH"
            export LD_LIBRARY_PATH="${runtimeLibraryPath}''${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
            export PYTHONPATH="$PWD/source''${PYTHONPATH:+:$PYTHONPATH}"

            echo "DENT-OIP dev shell ready. Run: make html"
          '';
        };
      });
}
