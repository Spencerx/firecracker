"""A test that ensures that all unit tests pass at integration time.

# TODO

- Run with `--release` once  `https://github.com/edef1c/libfringe/issues/75`
  is fixed
"""

import os

from subprocess import run

import pytest

import host_tools.cargo_build as host  # pylint: disable=import-error


CARGO_UNITTEST_REL_PATH = os.path.join(host.CARGO_BUILD_REL_PATH, "test")


@pytest.mark.timeout(240)
def test_unittests(test_session_root_path):
    """Run all unit tests from all Rust crates in the repo."""
    run(
        'CARGO_TARGET_DIR={} RUST_BACKTRACE=1 cargo test --all --no-fail-fast'
        .format(
            os.path.join(test_session_root_path, CARGO_UNITTEST_REL_PATH),
        ),
        shell=True,
        check=True
    )