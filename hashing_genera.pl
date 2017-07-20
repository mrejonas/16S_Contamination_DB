#!/usr/bin/perl
use warnings ;

foreach $in(@ARGV){
  $out = $in;
  $out =~ s/map/count/;
  open(IN, $in);
  open(OUT, ">>$out");
  while(<IN>){
    chomp;
    $genus = (split)[-1];
    if(!exists $hash{$genus}){
      $hash{$genus = 1};
    }else{
      $hash{$genus}++;
    }
  }
  close(OUT);
  close(IN);
}
