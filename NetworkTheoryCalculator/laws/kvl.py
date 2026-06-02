"""Kirchhoff's Voltage Law utilities."""

def kvl(loop_voltages):
    """Return the algebraic sum of voltages around a loop (should be zero)."""
    return sum(loop_voltages)
