# Ryan Proffitt
# 1 June 2021
# This code gives various tools for scheduling and analyzing satellite pass data.

# Gets the maximum bandwidth across a set of satellite passes
#   Each pass has a satellite ID, start time, end time, and downlink rate
# TODO: I feel like there is recursive solution that would be better
#       than making an array of start and end times due to overlaps
def get_max_necessary_bandwidth(pass_schedule):
    max_bandwidth_required = 0

    if len(pass_schedule) == 0:
        return max_bandwidth_required

    times_where_bandwidth_req_changes = []
    for sat_pass in pass_schedule:
        times_where_bandwidth_req_changes.append((sat_pass[1], sat_pass[3]))
        times_where_bandwidth_req_changes.append((sat_pass[2], -sat_pass[3]))

    sorted_bandwidth_req_changes = sorted(times_where_bandwidth_req_changes, key=lambda x: x[0])

    curr_bandwidth_required = 0
    for bandwidth_change in sorted_bandwidth_req_changes:
        curr_bandwidth_required += bandwidth_change[1]
        if curr_bandwidth_required > max_bandwidth_required:
            max_bandwidth_required = curr_bandwidth_required

    return max_bandwidth_required