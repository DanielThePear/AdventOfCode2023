#include <stdio.h>
#include <limits.h>
#include <unistd.h>
#include <stdlib.h>


typedef struct {
    long long dest_start;
    long long src_start;
    long long range;
} Mapping;

typedef struct {
    int group_length;
    Mapping *group_array;
} MappingGroup;

typedef struct {
    int groups_amount;
    MappingGroup **groups_array;
} Groups;

typedef struct {
    int seeds_amount;
    long long seeds_array[][2];
} Seeds;


long long compute_minimum_location(Groups *groups, Seeds *seeds);
void process_mapping(MappingGroup *maps, long long in_val, long long *out_val);


long long compute_minimum_location(Groups *groups, Seeds *seeds)
{
    long long lowest_location = LLONG_MAX;

    for (int s = 0; s < seeds->seeds_amount; s++)
    {
        printf("Working on seed %d\n", s + 1);
        long percent_indices = seeds->seeds_array[s][1] / 100;
        for (long long j = 0; j < seeds->seeds_array[s][1]; j++)
        {
            if (j % percent_indices == 0) printf("%lld%% done seed %d\n", j / percent_indices, s + 1);
            long long curr_val = seeds->seeds_array[s][0] + j;
            for (int k = 0; k < groups->groups_amount; k++) process_mapping(groups->groups_array[k], curr_val, &curr_val);
            lowest_location = (curr_val < lowest_location) ? curr_val : lowest_location;
        }
    }

    return lowest_location;
}


void process_mapping(MappingGroup *maps, long long in_val, long long *out_val)
{
    for (int i = 0; i < maps->group_length; i++)
    {
        Mapping curr_mapping = maps->group_array[i];
        if (!(in_val >= curr_mapping.src_start && in_val < curr_mapping.src_start + curr_mapping.range)) continue;
        *out_val = curr_mapping.dest_start + (in_val - curr_mapping.src_start);
        return;
    }
    *out_val = in_val;
}