from io import StringIO

from django.core.management import call_command


def test_no_pending_migrations(db):
    out = StringIO()
    err = StringIO()  # Capture stderr as well

    try:
        call_command("makemigrations", "--check", stdout=out, stderr=err)
    except SystemExit as e:
        output_str = out.getvalue()
        error_str = err.getvalue()

        # Check for specific "No changes detected" message (or customize)
        if "No changes detected" in output_str:
            # Expected: No pending migrations
            return  # Test passes

        # Check for specific error messages related to migrations
        expected_error_messages = [
            "You have pending migrations",  # Example 1
            "Migrations are not up to date",  # Example 2
            # ... add more expected messages
        ]

        found_expected_error = False

        for expected_message in expected_error_messages:
            if expected_message in error_str:
                found_expected_error = True
                break

        if not found_expected_error:
            raise AssertionError(
                f"Unexpected output from makemigrations:\nStdout: {output_str}\nStderr: {error_str}"
            ) from e  # Re-raise the original SystemExit

        raise AssertionError(f"Pending migrations detected:\n{error_str}") from e  # Include stderr in the error

    # If SystemExit is not raised, it means there are no pending migrations
    # and the test should pass (no assertion needed).
